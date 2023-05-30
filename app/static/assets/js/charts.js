
var chart6 = document.getElementById("radarchart");
console.log(chart6)
// new
var myChart6 = new Chart(chart6, {
type: 'radar',
data: {
    labels: ['Age 18-24', 'Age 25-31', 'Age 32-38', 'Age 39-45', 'Age 46-100+'],
    datasets: [{
        data: ["26", "35", "25", "28", "18"],
        backgroundColor: "rgba(48, 164, 255, 0.2)",
        borderColor: "rgba(48, 164, 255, 0.8)",
    }]
},
options: {
    animation: {
        duration: 2000,
        easing: 'easeOutQuart',
    },
    plugins: {
        legend: {
            display: false,
            position: 'right',
        },
        title: {
            display: true,
            text: 'Age Groups',
            position: 'top',
        },
    },
}
});
