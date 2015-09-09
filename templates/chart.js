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
            tick: {
                format: '%Y-%m-%d'
            }
        }
    }
});
