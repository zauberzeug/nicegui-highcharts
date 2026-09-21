import { convertDynamicProperties } from "../../static/utils/dynamic_properties.js";
import { Highcharts, loadMore, loadModule } from "nicegui-highcharts";

export default {
  template: "<div></div>",
  async mounted() {
    if (this.extras) {
      await loadMore();
    }
    for (const extra of this.extras) {
      await loadModule(extra);
    }
    convertDynamicProperties(this.options, true);
    // Tailwind's CSS reset makes form controls transparent, so the native inputs Highcharts overlays on the
    // range selector's date labels stop covering them. Highcharts merges inputStyle last into the input's
    // inline style, so this beats the reset; default to the chart's background to stay readable when dark.
    const background = this.options.chart?.backgroundColor ?? Highcharts.getOptions().chart?.backgroundColor;
    this.options.rangeSelector = {
      ...this.options.rangeSelector,
      inputStyle: {
        backgroundColor: Highcharts.color(background).rgba[3] === 1 ? background : "#fff",
        ...this.options.rangeSelector?.inputStyle,
      },
    };
    this.options.plotOptions = this.options.plotOptions ?? {};
    this.options.plotOptions.series = this.options.plotOptions.series ?? {};
    this.options.plotOptions.series.point = this.options.plotOptions.series.point ?? {};
    this.options.plotOptions.series.point.events = this.options.plotOptions.series.point.events ?? {};
    function uncycle(e) {
      // Highcharts events are cyclic, so we need to uncycle them
      let { point, target, ...rest } = e;
      point = point ?? target;
      return {
        ...rest,
        point_index: point?.index,
        point_x: point?.x,
        point_y: point?.y,
        series_index: point?.series?.index,
      };
    }
    this.options.plotOptions.series.point.events.click = (e) => this.$emit("pointClick", uncycle(e));
    this.options.plotOptions.series.point.events.dragStart = (e) => this.$emit("pointDragStart", uncycle(e));
    this.options.plotOptions.series.point.events.drag = (e) => this.$emit("pointDrag", uncycle(e));
    this.options.plotOptions.series.point.events.drop = (e) => this.$emit("pointDrop", uncycle(e));
    this.chart = Highcharts[this.type](this.$el, this.options);
    this.chart.reflow();
  },
  beforeDestroy() {
    this.destroyChart();
  },
  beforeUnmount() {
    this.destroyChart();
  },
  methods: {
    update_chart() {
      if (this.chart) {
        convertDynamicProperties(this.options, true);
        this.chart.update(this.options, true, true);
      }
    },
    destroyChart() {
      if (this.chart) {
        this.chart.destroy();
      }
    },
  },
  props: {
    type: String,
    options: Object,
    extras: Array,
  },
};
