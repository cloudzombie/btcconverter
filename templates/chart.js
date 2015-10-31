var chart = c3.generate({
	data: {
		xs: {
			'Actual Price': 'Date',
			'Linear Regression': 'PDate',
			'RSI 14': 'Date'
		},
		columns: [
			{{ actualtime }},
			{{ actualprice }}
		],
		axes: {
			'RSI 14': 'y2'
		},
		colors: {
			'Actual Price': '#0d87e9',
			'Linear Regression': '#888888',
			'RSI 14': '#439a46'
		},
	},

	subchart: {
		show: true
	},

	axis: {
		x: {
			type: 'timeseries',
			label: 'Date',
			tick: {
				format: '%Y-%m-%d'
			}
		},
		y: {
			label: {
				text: 'BTC Price',
				position: 'outer-middle'
			},
			tick:{
				format: d3.format("$.2f")
			}
		},
		y2: {
			show: true,
			default: [0, 100],
			label: {
				text: 'RSI 14', position: 'outer-middle'
			},
			tick: {
				values: [0,20,40,60,80,100],
				format: d3.format(".2f")
			}
		}
	},

	grid: {
		y: {
			lines: [{
				value: 30, text: 'RSI 30', axis: 'y2', position: 'start'
			},
			{
				value: 70, text: 'RSI 70', axis: 'y2', position: 'start'
			}
		]}
	}
});

setTimeout(function () {
	chart.load({
		columns: [
		{{ predictiontime }},
		{{ predictionpricelist }}
		]
	});
}, 700);


setTimeout(function () {
	chart.load({
		columns: [
		{{ actualtime }},
		{{ rsilist }}
		]
	});
}, 1200);
