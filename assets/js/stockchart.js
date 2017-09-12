var chart = AmCharts.makeChart( "chartdiv", {
  "type": "stock",
  "theme": "light",
  "categoryAxesSettings": {
    "minPeriod": "mm"
  },

  "dataSets": [ {
    "fieldMappings": [ {
      "fromField": "sellvalue",
      "toField": "sellvalue"
    },{
      "fromField": "buyvalue",
      "toField": "buyvalue"
    }, {
      "fromField": "volume",
      "toField": "volume"
    } ],
    "dataProvider": data_array,
    "categoryField": "date"
  }],

  "panels": [ {
    "showCategoryAxis": false,
    "title": "Value",
    "percentHeight": 70,

    "stockGraphs": [ {
      "id": "g1",
      "valueField": "buyvalue",
      "lineColor": "#e20413",
      "type": "smoothedLine",
      "lineThickness": 2,
      "bullet": "round",
      "balloonText": "Buy: <b>[[value]]</b>",
      "useDataSetColors": false
    },{
      "id": "g2",
      "valueField": "sellvalue",
      "lineColor": "#0dbf03",
      "type": "smoothedLine",
      "lineThickness": 2,
      "bullet": "round",
      "balloonText": "Sell: <b>[[value]]</b>",
      "useDataSetColors": false
    }],

    "stockLegend": {
      "valueTextRegular": " ",
      "markerType": "none"
    }
  }, {
    "title": "Volume",
    "percentHeight": 30,
    "stockGraphs": [ {
      "valueField": "volume",
      "type": "column",
      "cornerRadiusTop": 2,
      "fillAlphas": 1
    } ],

    "stockLegend": {
      "valueTextRegular": " ",
      "markerType": "none"
    }
  } ],

  "chartScrollbarSettings": {
    "graph": "g1",
    "usePeriod": "mm",
    "position": "top"
  },

  "chartCursorSettings": {
    "valueBalloonsEnabled": true
  },

  "periodSelector": {
    "position": "top",
    "dateFormat": "YYYY-MM-DD JJ:NN",
    "inputFieldWidth": 150,
    "periods": [ {
      "period": "hh",
      "count": 1,
      "label": "1 hour"
    }, {
      "period": "hh",
      "count": 2,
      "label": "2 hours"
    }, {
      "period": "hh",
      "count": 5,
      "label": "5 hour"
    }, {
      "period": "hh",
      "count": 12,
      "label": "12 hours"
    }, {
      "period": "hh",
      "count": 24,
      "label": "24 hours"
    }, {
      "period": "hh",
      "count": 48,
      "selected": true,
      "label": "48 hours"
    }, {
      "period": "MAX",
      "label": "MAX"
    } ]
  },

  "panelsSettings": {
    "usePrefixes": false
  },
  "dataSetSelector": {
    "position": "left"
  },

  "export": {
    "enabled": true,
    "position": "bottom-left"
  }
} );

function _show_map(){
    document.getElementById("chartLoader").style.display = "none";
    document.getElementById("chartdiv").style.display = "inline-block";
}

setTimeout(_show_map, 3000);