var modelColumnsType =
{
    'Name':'text',
    'Last Name':'text',
    'Identity Number':'text',
    'Age':'number',
    'Country':'text',
    'Province':'text',
    'Municipality':'text',
    'Situation':'text',
    'State':'text',
    'Address':'text',
    'Birth Date':'date',
    'Group':'text',
    'Career':'text',
    'Faculty':'text',
    'Course Type':'text',
    'Email':'text',
    'Source of Income':'text',
    'Academic Origin':'text',
    'Study Regimen':'text',
    'Natural From':'text',
    'Phone Number':'text',
    'ES Income Date':'date',
    'Civil State':'text',
    'Political Organization':'text',
    'CES Income Date':'date',
    'Enrollment Date':'date',
    'Sex':'text',
    'Skin Color':'text',
    'Student Type':'text',
    'Study Year':'number',
    'Work Center':'text',
    'Fathers Name':'text',
    'Fathers Academic Level':'text',
    'Mothers Name':'text',
    'Mothers Academic Level':'text',
    'Military Service Type':'text'
}

var columnsToFields = 
{
    'Name':'name',
    'Last Name':'last_Name',
    'Identity Number':'identity_Number',
    'Age':'age',
    'Country':'country',
    'Province':'province',
    'Municipality':'municipality',
    'Situation':'situation',
    'State':'state',
    'Address':'address',
    'Birth Date':'birth_Date',
    'Group':'group',
    'Career':'career',
    'Faculty':'faculty',
    'Course Type':'course_Type',
    'Email':'mail',
    'Source of Income':'source_of_Income',
    'Academic Origin':'academic_Origin',
    'Study Regimen':'study_Regimen',
    'Natural From':'natural_From',
    'Phone Number':'phone_Number',
    'ES Income Date':'es_Income_Date',
    'Civil State':'civil_State',
    'Political Organization':'political_Organization',
    'CES Income Date':'ces_Income_Date',
    'Enrollment Date':'enrollment_Date',
    'Sex':'sex',
    'Skin Color':'skin_Color',
    'Student Type':'student_Type',
    'Study Year':'study_Year',
    'Work Center':'work_Center',
    'Fathers Name':'fathers_Name',
    'Fathers Academic Level':'fathers_Academic_Level',
    'Mothers Name':'mothers_Name',
    'Mothers Academic Level':'mothers_Academic_Level',
    'Military Service Type':'military_Service_Type'
}

var fieldsOptimize = document.getElementById('fieldOptimize')
var keysFields = Object.keys(columnsToFields)
for(let i = 0; i < keysFields.length; i++)
{
    fieldsOptimize.innerHTML += `<option value=${columnsToFields[keysFields[i]]}>${keysFields[i]}</option>`
}

var columnTypeToHtml=
{
    'text':`<input type="text" onChange="changeFilterValue"/>`,

    'date':` <input class="since" type="date" onChange="changeFilterValue"/>
    -
    <input class="to" type="date" onChange="changeFilterValue"/>`,

    'number':`<input class="since" type="Number" onChange="changeFilterValue"/>
    -
    <input class="to" type="Number" onChange="changeFilterValue"/>`
}

var trs = document.getElementsByTagName('tr')
var ths = trs[0].getElementsByTagName("th")

var initialColumns = ['Identity Number', 'Name', 'Last Name', 'Age', 'Province', 'Municipality']
var columnsOn = []
var columnsOut = []
var checked = {}
for(let i = 0; i< ths.length; i++)
{
    if(!initialColumns.includes(ths[i].innerHTML))
        columnsOut.push(ths[i].innerHTML)
}

for(let i = 0; i < initialColumns.length; i++)
    columnsOn.push(initialColumns[i])

console.log(columnsOn)
var students = []

for(let i = 1; i < trs.length; i++)
{
    let s = {}
    let tds = trs[i].getElementsByTagName('td')
    for(j = 0; j < tds.length; j++)
    {
        if(tds[j].getElementsByTagName('a').length === 0)
            s[ths[j].innerHTML] = tds[j].innerHTML

        else
            s.id = tds[j].id
        
    }
    students.push(s)
    checked[s.id] = false
}

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
    trHead.innerHTML += `<th class="noParse" scope="col"></th>`

    for(let i = 0; i < columnsOn.length; i++)
        trHead.innerHTML += `<th scope="col">${columnsOn[i]}</th>`
      
    for(let j = 0; j < students.length; j++)
    {
        trBody = document.createElement('tr');
        trBody.innerHTML += `<td class="noParse">
        <input id='${students[j].id}' type="checkbox" onChange="checkStudent(${students[j].id})"/>
     </td>`
        for(let i = 0; i < columnsOn.length; i++)
            trBody.innerHTML += ` <td>${students[j][columnsOn[i]]}</td>`

        trBody.innerHTML += `<td style="display:flex"><a type="button" class="btn btn-warning" href="/student-update/${students[j].id}">Editar</a>
        <a type="button" class="btn btn-danger" href="/student-delete/${students[j].id}">Eliminar</a>
    </td>`
        tBody.appendChild(trBody)
    
    if(checked[students[j].id])    
        document.getElementById(`${students[j].id}`).checked=1
    }
}

function changeFilterName(select)
{
    let filterItem = select.parentNode
    let valueContainer = filterItem.getElementsByClassName('valueContainer')[0]
    valueContainer.innerHTML=''
    valueContainer.innerHTML = columnTypeToHtml[modelColumnsType[select.value]]
}

function addFilter()
{
    let filtersContainer = document.getElementById('filtersContainer');
    let filterItem = document.createElement('div')
    filterItem.className = "filterItem"
    let selectFilter = document.createElement('select');
    
    let filtersName = Object.keys(modelColumnsType);
    for(let i = 0; i < filtersName.length; i++)
    {
        selectFilter.innerHTML += `<option id=${filtersName[i]}>${filtersName[i]}</option>`
    }
    
    filterItem.appendChild(selectFilter)
    filterItem.innerHTML += ` <div class="valueContainer" style="display:flex"> 
    <input type="text" onChange="changeFilterValue"/>
    </div>
    <div class="buttonRemove" onClick='removeFilter(this)'>-</div>`
    filterItem.addEventListener
    filtersContainer.appendChild(filterItem)
    let selects = filtersContainer.getElementsByTagName('select');
    selects[selects.length - 1].addEventListener('change', changeFilterName.bind(this, selects[selects.length - 1]))

}

function removeFilter(element)
{
    let filtersContainer = document.getElementById('filtersContainer');
    filtersContainer.removeChild(element.parentNode)
}

function checkStudent(id)
{
    checked[id] = !checked[id]
}

function optimize()
{
    var cant_groups = document.getElementById('postCantGroups').value
    var property = document.getElementById('fieldOptimize').value
    var id_students = []
    const csrftoken = getCookie('csrftoken')
    for(let i = 0; i < students.length; i++)
    {
        if(checked[students[i].id])
            id_students.push(Number(students[i].id))
    }

    fetch('/optimize', 
    {
        method:'POST',
        body: JSON.stringify({
            cant_groups:cant_groups,
            id_students:id_students,
            property:property
        }),
        headers:
        {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken
        }
    })
}

updateColumnsAddRemove()
udpateTable()

function getCookie(name) { var cookieValue = null; if (document.cookie && document.cookie !== '') { var cookies = document.cookie.split(';'); for (var i = 0; i < cookies.length; i++) { var cookie = cookies[i].trim(); if (cookie.substring(0, name.length + 1) === (name + '=')) { cookieValue = decodeURIComponent(cookie.substring(name.length + 1)); break; } } } return cookieValue; }