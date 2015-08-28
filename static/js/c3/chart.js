var chart = c3.generate({
    data: {
        x: 'Date',
        columns: [
            ['Date', '2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04', '2013-01-05', '2013-01-06'],
            ['Actual', 30, 200, 100, 400, 150, 250],
            ['Prediction', 130, 340, 200, 600, 250, 350]
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

/*
setTimeout(function () {
    chart.load({
        columns: [
            ['data3', 400, 500, 450, 700, 600, 500]
        ]
    });
}, 1000)
*/
