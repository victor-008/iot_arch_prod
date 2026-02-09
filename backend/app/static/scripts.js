// // recconection and history loadings script

// async function loadHistory(){
//     const res = await fetch("/history");
//     const data = await res.json();

//     data.reverse().forEach(d=>{
//         chart.data.labels.push(d.timestamp);
//         chart.data.datasets[1].data.push(d.temperature);
//         chart.data.datasets[2].data.push(d.humidity);
//     });
//     chart.update();
// }

// loadHistory();

// function connectWS(){
//     const ws = new WebSocket("WS://127.0.0.1:8000/ws");

//     ws.onmessage = (event)=>{
//         const data = JSON.parse(event.data);
//         chart.data.labels.push(data.timestamp);
//         chart.data.datasets[1].data.push(data.temperature);
//         chart.data.datasets[2].data.push(data.humidity);
//         chart.update();
//     }
//     ws.onclose = ()=>{
//         setTimeout(connectWS, 3000);
//     }
// }

// connectWS();


const ctx=document.getElementById('chart');

const chart=new Chart(ctx,{
type:'line',
data:{labels:[],datasets:[
{label:'Temp',data:[]},
{label:'Humidity',data:[]}
]}
});

function connect(){
const ws=new WebSocket("ws://localhost:8000/ws");

ws.onmessage=(e)=>{
const d=JSON.parse(e.data);
chart.data.labels.push(new Date().toLocaleTimeString());
chart.data.datasets[0].data.push(d.temperature);
chart.data.datasets[1].data.push(d.humidity);
chart.update();


document.getElementById('temp-value').innerText =
    data.temperature + " °C";

document.getElementById('hum-value').innerText =
    data.humidity + " %";

document.getElementById('timestamp').innerText =
    new Date().toLocaleTimeString();

document.getElementById('status-indicator').style.background="lime";
document.getElementById('status-text').innerText="Connected";




};

ws.onclose=()=>{
    ws.onclose = () => {
    document.getElementById('status-indicator').style.background="red";
    document.getElementById('status-text').innerText="Disconnected";
};

}
    setTimeout(connect,3000);
}

connect();
