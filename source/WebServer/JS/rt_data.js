function start_graph(){
    setInterval(run_graph, 1000);
}

function run_graph(){

    const xhttp = new XMLHttpRequest();
    xhttp.open('GET',`http://127.0.0.1:5000//pm10pm2p5`,true);

    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){

            let response = JSON.parse(this.responseText);
            console.log(response.pm2p5);
            console.log(response.pm10);

            let ctx = 'pm_chart';
            let chart = new Chart(ctx,
                {
                    type: 'line',// The type of chart we want to create
                    data: {
                        labels: response.pm2p5,
                        datasets: [{
                            lineTension: 0,
                            label: 'pm2.5',
                            fill: false,
                            backgroundColor: 'red',
                            borderColor: 'red',
                            data: response.pm2p5
                        },{
                            lineTension: 0,
                            label: 'pm10',
                            fill: false,
                            backgroundColor: 'blue',
                            borderColor: 'blue',
                            data: response.pm10
                        }]
                    },
                    options: {
                        animation: {
                            duration: 0, // general animation time
                        },
                        hover: {
                            animationDuration: 0, // duration of animations when hovering an item
                        },
                        responsiveAnimationDuration: 0, // animation duration after a resize
                    }
                }
            );
        }
        else{
            console.log("something wrong");
        }
    };
    xhttp.send();
}
