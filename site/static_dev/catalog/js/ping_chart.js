function JoinTime(hour, minute) {
    function toStandartView(number) {
        let stringNumber = String(number);
        if (stringNumber.length == 1) {
            stringNumber = '0' + stringNumber;
        }
        return stringNumber;
    }

    return toStandartView(hour) + ':' + toStandartView(minute);
}

const ctx = document.getElementById('myChart');
const data = JSON.parse(document.querySelector('#jsonData').getAttribute('data-json'));

new Chart(ctx, {
    type: 'line',
    data: {
        labels: data.map(row => JoinTime(row.hour, row.minute)),
        datasets: [{
        label: 'Пинг за последние 24 часа',
        data: data.map(row => row.ping),
        borderWidth: 1,
        }]
    }
});