var chart2 = document.getElementById('barchart')

// new
var myChart2 = new Chart(chart2, {
type: 'bar',
data: {
    labels: ['Распределение'],
    datasets: [{
            label: 'Экономика',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: [
              'rgb(255, 99, 132)',
            ],
            borderWidth: 1,
            data: "4",
        }, {
            label: 'Программирование',
            backgroundColor: 'rgba(255, 159, 64, 0.2)',
            borderColor: [
              'rgb(255, 159, 64)',
            ],
            borderWidth: 1,
            data: "5",
        }, {
            label: 'Машинное обучение',
            backgroundColor: 'rgba(255, 205, 86, 0.2)',
            borderColor: [
              'rgb(255, 205, 86)',
            ],
            borderWidth: 1,
            data: "3",
        }, {
            label: 'Математический анализ',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: [
              'rgb(75, 192, 192)',
            ],
            borderWidth: 1,
            data: "4",
        }, {
            label: 'Алгоритмы и структуры данных',
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: [
              'rgb(54, 162, 235)',
            ],
            borderWidth: 1,
            data: "4",
        }
        ]
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
            text: 'Оценка',
            position: 'left',
        },
    },
}
});

