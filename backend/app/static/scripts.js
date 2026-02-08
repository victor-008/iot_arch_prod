async function loadHistory(){
    const res = await fetch("/history");
    const data = await res.json();

    data.reverse().forEach(d=>{
        chart.data.labels.push(d.timestamp);
        chart.data.datasets[1].data.push(d.temperature);
        chart.data.datasets[2].data.push(d.humidity);
    });
    chart.update();
}

loadHistory();

function connectWS(){
    const ws = new WebSocket("WS://127.0.0.1:8000/ws");

    ws.onmessage = (event)=>{
        const data = JSON.parse(event.data);
        chart.data.labels.push(data.timestamp);
        chart.data.datasets[1].data.push(data.temperature);
        chart.data.datasets[2].data.push(data.humidity);
        chart.update();
    }
    ws.onclose = ()=>{
        setTimeout(connectWS, 3000);
    }
}

connectWS();