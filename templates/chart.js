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
