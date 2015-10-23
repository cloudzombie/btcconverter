var chart = c3.generate({
	data: {
		xs: {
			'Actual Price': 'Date',
			'Linear Regression': 'PDate'
		},
		columns: [
			{{ actualtime }},
			{{ actualprice }}
		]},

		subchart: {
			show: true
		},

		axis: {
			x:
			{ type: 'timeseries', label: 'Date', tick: { format: '%Y-%m-%d'}
		},
			y:
			{ label: { text: 'BTC Price', position: 'outer-middle' },
				tick:
				{ format: d3.format("$.2f") }
		},
			y2:
			{ show:true,
				default: [0, 100],
				label: {
					text: 'RSI', position: 'outer-middle'
				},
				tick:{
					values: [0,20,40,60,80,100]
				}
			}
		}
});

setTimeout(function () {
	chart.load({
		columns: [
			{{ predictiontime }},
			{{ predictionpricelist }}
		],
		point: {
			show: false
		},
		tooltip: {
			format: {
				title: function (d) { return 'Linear Regression' + d; },
				value: function (value, ratio, id) {
					var format = id === 'Linear Regression' ? d3.format('$') : d3.format('$');
					return format(value);}
				}
			}
		});
}, 1000);
