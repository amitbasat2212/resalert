class graph{
create_pie_chart(lables_name:any[],data:any[]){
new Chart(document.getElementById("pie-chart") as any, {
    type: 'pie',
    data: {
      labels:lables_name,
      datasets: [{
        label: "Population in work",
        backgroundColor: ["#3e95cd", "#8e5ea2"],
        data: data
      }]
    },
    options: {
      title: {
        display: true,
        text: 'number of men vs women in work'
      }
    }
});
}

create_bar_chart(labels:any,data:any){
    new Chart(document.getElementById("bar-chart") as any, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label:"said how much in each daprtment",
            data: data,
            backgroundColor: [
              'rgba(255, 99, 132, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(255, 206, 86, 0.2)',
              'rgba(75, 192, 192, 0.2)',
              'rgba(153, 102, 255, 0.2)',
              'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
              'rgba(255,99,132,1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)',
              'rgba(153, 102, 255, 1)',
              'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
          }]
        },
        options: {
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true
              }
            }]
          }
        }
      });
    }
}