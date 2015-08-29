var chart = c3.generate({
    data: {
        x: 'Date',
        columns: [
            {{ actualtime }},
            {{ actualprice }}
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
