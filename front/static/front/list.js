
var trs = document.getElementsByTagName('tr')
var ths = trs[0].getElementsByTagName("th")

var columnsOn = []
for(let i = 0; i< ths.length; i++)
    columnsOn.push(ths[i].innerHTML)

var columnsOut = []


var students = []

for(let i = 1; i < trs.length; i++)
{
    let s = {}
    let tds = trs[i].getElementsByTagName('td')
    for(j = 0; j < tds.length; j++)
    {
        if(tds[j].getElementsByTagName('a').length === 0)
            s[ths[j].innerHTML] = tds[j].innerHTML
        
    }
    students.push(s)
}

console.log(students)

function updateColumnsAddRemove()
{
    var addContainer = document.getElementById("addColumnsContainer");
    var removeContainer = document.getElementById("removeColumnsContainer");

    addContainer.innerHTML = ''
    removeContainer.innerHTML = ''

    for(let i = 0; i < columnsOn.length; i++)
    {
        removeContainer.innerHTML += `
        <div class="itemRemove" onClick='removeColumn(this)'>
            <div class="buttonRemove">-</div>
            <p>${columnsOn[i]}</p>
        </div>
        `
    }

    for(let i = 0; i < columnsOut.length; i++)
    {
        addContainer.innerHTML += `
        <div class="itemAdd" onClick='addColumn(this)'>
            <div class="buttonAdd">+</div>
            <p>${columnsOut[i]}</p>
        </div>
        `
    }

    if(columnsOut.length)
        addContainer.style.marginTop = '1rem'
}

function removeColumn(columnContainer)
{
    let c = columnContainer.getElementsByTagName('p')[0].innerHTML;
    columnsOn = columnsOn.filter(m=>m!=c)
    columnsOut.push(c)

    updateColumnsAddRemove()
    udpateTable()
}

function addColumn(columnContainer)
{
    let c = columnContainer.getElementsByTagName('p')[0].innerHTML;
    columnsOut = columnsOut.filter(m=>m!=c)
    columnsOn.push(c)

    updateColumnsAddRemove()
    udpateTable()
}

function udpateTable()
{
    let tHead = document.getElementsByTagName("thead")[0]
    let tBody = document.getElementsByTagName('tbody')[0]

    tHead.innerHTML = '<tr></tr>'
    tBody.innerHTML = ''

    let trHead = tHead.getElementsByTagName('tr')[0]

    for(let i = 0; i < columnsOn.length; i++)
        trHead.innerHTML += `<th scope="col">${columnsOn[i]}</th>`
      
    for(let j = 0; j < students.length; j++)
    {
        trBody = document.createElement('tr');

        for(let i = 0; i < columnsOn.length; i++)
            trBody.innerHTML += ` <td>${students[j][columnsOn[i]]}</td>`

        tBody.appendChild(trBody)
        
    }

}

updateColumnsAddRemove()