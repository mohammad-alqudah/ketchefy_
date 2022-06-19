function getChartColorsArray(e) {
  if (null !== document.getElementById(e)) {
    e = document.getElementById(e).getAttribute("data-colors");
    if (e)
      return (e = JSON.parse(e)).map(function (e) {
        var t = e.replace(" ", "");
        if (-1 === t.indexOf(",")) {
          var a = getComputedStyle(document.documentElement).getPropertyValue(
            t
          );
          return a || t;
        }
        e = e.split(",");
        return 2 != e.length
          ? t
          : "rgba(" +
              getComputedStyle(document.documentElement).getPropertyValue(
                e[0]
              ) +
              "," +
              e[1] +
              ")";
      });
  }
}

var linechartDashedColors = getChartColorsArray("line_chart_dashed");
linechartDashedColors &&
  ((options = {
    chart: {
      height: 380,
      type: "line",
      zoom: { enabled: !1 },
      toolbar: { show: !1 },
    },
    colors: linechartDashedColors,
    dataLabels: { enabled: !1 },
    stroke: { width: [3, 4, 3], curve: "straight" },
    series: [
      {
        name: "Session Duration",
        data: [45, 52, 38, 24, 33, 26, 21, 20, 6, 8, 15, 10],
      },
      {
        name: "Page Views",
        data: [36, 42, 60, 42, 13, 18, 29, 37, 36, 51, 32, 35],
      },
      {
        name: "Total Visits",
        data: [89, 56, 74, 98, 72, 38, 64, 46, 84, 58, 46, 49],
      },
    ],
    title: {
      text: "Page Statistics",
      align: "left",
      style: { fontWeight: 500 },
    },
    markers: { size: 0, hover: { sizeOffset: 6 } },
    xaxis: {
      categories: [
        "01 Jan",
        "02 Jan",
        "03 Jan",
        "04 Jan",
        "05 Jan",
        "06 Jan",
        "07 Jan",
        "08 Jan",
        "09 Jan",
        "10 Jan",
        "11 Jan",
        "12 Jan",
      ],
    },
    tooltip: {
      y: [
        {
          title: {
            formatter: function (e) {
              return e + " (mins)";
            },
          },
        },
        {
          title: {
            formatter: function (e) {
              return e + " per session";
            },
          },
        },
        {
          title: {
            formatter: function (e) {
              return e;
            },
          },
        },
      ],
    },
    grid: { borderColor: "#f1f1f1" },
  }),
  (chart = new ApexCharts(
    document.querySelector("#line_chart_dashed"),
    options
  )).render());

var options_2 =
  [
    {
      name: "Session Duration",
      data: [45, 52, 38, 24, 33, 26, 21, 20, 6, 8, 15, 10],
    },
    {
      name: "Total Visits",
      data: [89, 56, 74, 98, 72, 38, 64, 46, 84, 58, 46, 49],
    },
  ];


var linechartDashedColors_2 = getChartColorsArray("line_chart_dashed_2");
linechartDashedColors_2 &&
  ((options = {
    chart: {
      height: 380,
      type: "line",
      zoom: { enabled: !1 },
      toolbar: { show: !1 },
    },
    colors: linechartDashedColors_2,
    dataLabels: { enabled: !1 },
    stroke: { width: [3, 4, 3], curve: "straight" },
    series: [
      {
        name: "Session Duration",
        data: [45, 52, 38, 24, 33, 26, 21, 20, 6, 8, 15, 10],
      },
      {
        name: "Page Views",
        data: [36, 42, 60, 42, 13, 18, 29, 37, 36, 51, 32, 35],
      },
      {
        name: "Total Visits",
        data: [89, 56, 74, 98, 72, 38, 64, 46, 84, 58, 46, 49],
      },
    ],
    title: {
      text: "Page Statistics",
      align: "left",
      style: { fontWeight: 500 },
    },
    markers: { size: 0, hover: { sizeOffset: 6 } },
    xaxis: {
      categories: [
        "01 Jan",
        "02 Jan",
        "03 Jan",
        "04 Jan",
        "05 Jan",
        "06 Jan",
        "07 Jan",
        "08 Jan",
        "09 Jan",
        "10 Jan",
        "11 Jan",
        "12 Jan",
      ],
    },
    tooltip: {
      y: [
        {
          title: {
            formatter: function (e) {
              return e + " (mins)";
            },
          },
        },
        {
          title: {
            formatter: function (e) {
              return e + " per session";
            },
          },
        },
        {
          title: {
            formatter: function (e) {
              return e;
            },
          },
        },
      ],
    },
    grid: { borderColor: "#f1f1f1" },
  }),
  (chart_2 = new ApexCharts(
    document.querySelector("#line_chart_dashed_2"),
    options
  )).render());


function updateChart_2(){

  chart_2.updateSeries(options_2);
}
