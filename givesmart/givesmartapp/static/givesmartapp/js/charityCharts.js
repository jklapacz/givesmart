/**
 * Created by sol on 3/20/16.
 */
/** @namespace google.charts */
/** @namespace google.charts.Bar */
function barChart(charities, elementId) {
    google.charts.load('current', {'packages': ['bar']});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'charity');
        // todo: actual metric
        data.addColumn('number', 'metric');
        for (var charityName in charities) {
            data.addRow([charityName, charities[charityName]]);
        }
        var options = {
            chartArea: {
                height: "100%"
            },
            chart: {
                title: 'Charity Comparison'
            }
        };

        var chart = new google.charts.Bar(document.getElementById(elementId));

        chart.draw(data, options);
    }
}