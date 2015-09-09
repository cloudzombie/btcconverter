var chart = c3.generate({
    data: {
        xs: {
            'Actual Price': 'Date',
            'Prediction Price': 'PDate'
        },
        columns: [
            {{ actualtime }},
            {{ actualprice }},
            {{ predictiontime }},
            {{ predictionpricelist }}
        ]
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
            tick: {
                format: d3.format("$")
        }
    }
}
});
