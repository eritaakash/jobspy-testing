console.log('Script loaded!');

async function callApi() {
    const res = await fetch('/api/jobs');
    const data = await res.json();
    
    const jobObjs = data.data;
    jobObjs.forEach(obj => {
        delete obj.description;
    });

    const table = createTable(jobObjs);

    const tableContainer = document.getElementById('table-container');
    tableContainer.innerHTML = '';

    tableContainer.appendChild(table);
    console.log('Table created and appended to container!');
}

function createTable(arrOfObjs) {
    const table = document.createElement('table');

    const headerRow = document.createElement('tr');
    const headers = Object.keys(arrOfObjs[0]);

    headers.forEach(header => {
        const th = document.createElement('th');
        th.textContent = header;
        headerRow.appendChild(th);
    });

    table.appendChild(headerRow);

    arrOfObjs.forEach(obj => {
        const row = document.createElement('tr');
        headers.forEach(header => {
            const td = document.createElement('td');
            td.textContent = obj[header];
            row.appendChild(td);
        });
        table.appendChild(row);
    });

    return table;
}