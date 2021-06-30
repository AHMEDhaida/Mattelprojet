
// chartjs initialization

$(function () {
    "use strict";


// doughnut_chart

    var ctx = document.getElementById("doughnut_chart");
    var data = {
        labels: [
            "En service", "Hors service", "En panne"
        ],
        datasets: [{
            data: [ {50, 10, 5],
            backgroundColor: [
                "#acf5fe",
                "#f79490",
                "#fcdd82",

            ],
            borderWidth: [
                "0px",
                "0px",
                "0px",

            ],
            borderColor: [
                "#acf5fe",
                "#f79490",
                "#fcdd82",

            ]
        }]
    };

    var myDoughnutChart = new Chart(ctx, {
        type: 'doughnut',
        data: data,
        options: {
            legend: {
                display: false
            }
        }
    });


});


