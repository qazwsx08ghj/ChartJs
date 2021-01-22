// not used

let x = [];
    let y = [];
    fetch('http://127.0.0.1:8000/api/datas/?format=json', {})
    .then((response) => {

        console.log(response);

    return response.json();
    }).then((data) => {
        data.forEach(d => x.push(d['number']));
        data.forEach(dv => y.push(dv['value']));
    });
    let ctx = document.getElementById('chart').getContext('2d');

    let chart = new Chart(ctx, {
        type: 'bar',
        data:{
            labels: x,
            datasets: [{
                label: '圖表',
                data: y,
            }]
        },
        options: {
            scales: {
                xAxes: [{
                            display: true,
                            scaleLabel: {
                                display: true,
                                labelString: 'number'
                            }
                        }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'value'
                    }
                }]
            }
        }
    }
    )