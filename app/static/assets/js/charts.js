var chart2 = document.getElementById('barchart')

// new
var myChart2 = new Chart(chart2, {
type: 'bar',
data: {
    labels: ['Экономика', 'Программирование', 'Машинное обучение', 'Математический анализ', 'Алгоритмы и структуры данных'],
    datasets: [{
            label: 'Income',
            backgroundColor: [
              'rgba(255, 99, 132, 0.2)',
              'rgba(255, 159, 64, 0.2)',
              'rgba(255, 205, 86, 0.2)',
              'rgba(75, 192, 192, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(153, 102, 255, 0.2)',
              'rgba(201, 203, 207, 0.2)'
            ],
            borderColor: [
              'rgb(255, 99, 132)',
              'rgb(255, 159, 64)',
              'rgb(255, 205, 86)',
              'rgb(75, 192, 192)',
              'rgb(54, 162, 235)',
              'rgb(153, 102, 255)',
              'rgb(201, 203, 207)'
            ],
            borderWidth: 1,
            data: ["4", "5", "4", "3", "4", "5", "5"],
        }]
},
options: {
    animation: {
        duration: 2000,
        easing: 'easeOutQuart',
    },
    plugins: {
        legend: {
            display: true,
            position: 'top',
        },
        title: {
            display: true,
            text: 'Revenue',
            position: 'left',
        },
    },
}
});

