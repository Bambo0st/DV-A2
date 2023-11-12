import EUR from "./dataFiles/EUR.json" assert {type: 'json'};
import NA from "./dataFiles/NorthAmerica.json" assert {type: 'json'};
import Asia from "./dataFiles/Asia.json" assert {type: 'json'};
import Continent from "./dataFiles/Continent.json" assert {type: 'json'};
import SA from "./dataFiles/SA.json" assert {type: 'json'};
import Africa from "./dataFiles/Africa.json" assert {type: 'json'};
import Oceana from "./dataFiles/Oceana.json" assert {type: 'json'};
import India from "./dataFiles/India.json" assert {type: 'json'};

const getDetails = (data) => {
    var sum = 0;
    const names = data.map(obj => obj.location);
    const values = data.map(obj => obj.total_cases);
    const deaths = data.map(obj => obj.total_deaths);
    const parents = data.map(obj => {
        if (obj.location == "")
            return "World"
        else return obj.continent
    })
    const date = data.map(obj => obj.date)
    const new_cases = data.map(obj => obj.new_cases);
    return [names, values, parents, deaths, date, new_cases]
}
var EUR_Details = getDetails(EUR)
var NA_Details = getDetails(NA)
var Asia_Details = getDetails(Asia)
var SA_Details = getDetails(SA)
var Africa_Details = getDetails(Africa)
var Oceana_Details = getDetails(Oceana)
var Continent_Details = getDetails(Continent)
var India_Details = getDetails(India)

var d1 = [{
    type: "treemap",
    branchvalues: 'total',
    labels: Continent_Details[0],
    parents: Continent_Details[2],
    values: Continent_Details[1],
    // textinfo: "label+value+percent parent+percent entry",
    textinfo: "label+value",
    // domain: { "x": [0, 0.6], "y": [0, 0.94] },
    // outsidetextfont: { "size": 20, "color": "#377eb8" },
    marker: { "line": { "width": 2 }, },
    pathbar: { "visible": false },
}];
const Vaccination_Details = Continent_Details.slice();
console.log(Vaccination_Details)
var labels1 = ["Vaccinated1", "Not Vaccinated1", "Asia", "Vaccinated2", "Not Vaccinated2", "Europe", "Vaccinated3", "Not Vaccinated3", "North America", "Vaccinated4", "Not Vaccinated4", "South America", "Vaccinated5", "Not Vaccinated5", "Africa", "Vaccinated6", "Not Vaccinated6", "Oceana"]
var values1 = [3118571898, 4721383370 - 3118571898, 4721383370, 487374943, 744807803 - 487374943, 744807803, 405860309, 600323657 - 405860309, 600323657, 330715925, 436816679 - 330715925, 436816679, 193994506, 1426736614 - 193994506, 1426736614, 26305230, 45038860 - 26305230, 45038860]
var parents1 = ["Asia", "Asia", "World", "Europe", "Europe", "World", "North America", "North America", "World", "South America", "South America", "World", "Africa", "Africa", "World", "Oceana", "Oceana", "World"]

const d6 = [{
    branchvalues: 'total',
    type: 'treemap',
    labels: labels1,
    textinfo: "label+value",
    parents: parents1,
    values: values1,
    outsidetextfont: { "size": 20, "color": "#377eb8" },
    marker: { "line": { "width": 2 } },
    pathbar: { "visible": false }
}];

var arr = [EUR_Details, NA_Details, Asia_Details, SA_Details, Africa_Details, Oceana_Details]
arr.forEach((e) => {
    for (var i = 0; i < 6; i++) {
        Continent_Details[i] = Continent_Details[i].concat(e[i])
    }
})
var d2 = [{
    type: "treemap",
    branchvalues: 'total',
    labels: Continent_Details[0],
    parents: Continent_Details[2],
    values: Continent_Details[1],
    // textinfo: "label+value+percent parent+percent entry",
    textinfo: "label+value",
    // domain: { "x": [0, 0.6], "y": [0, 0.94] },
    outsidetextfont: { "size": 20, "color": "#377eb8" },
    marker: { "line": { "width": 2 } },
    pathbar: { "visible": false },

}];
var d3 = [{
    type: "treemap",
    branchvalues: 'total',
    labels: Continent_Details[0],
    parents: Continent_Details[2],
    values: Continent_Details[3],
    // textinfo: "label+value+percent parent+percent entry",
    textinfo: "label+value",
    // domain: { "x": [0, 0.6], "y": [0, 0.94] },
    outsidetextfont: { "size": 20, "color": "#377eb8" },
    marker: { "line": { "width": 2 } },
    pathbar: { "visible": false }
}];
var d4 = [{
    type: "treemap",
    branchvalues: 'total',
    labels: Asia_Details[0],
    parents: Asia_Details[2],
    values: Asia_Details[3],
    // textinfo: "label+value+percent parent+percent entry",
    textinfo: "label+value",
    // domain: { "x": [0, 0.6], "y": [0, 0.94] },
    outsidetextfont: { "size": 20, "color": "#377eb8" },
    marker: { "line": { "width": 2 } },
    pathbar: { "visible": false }
}];

const casesByMonthAndDate = {};

India_Details[4].forEach((date, index) => {
    // Extract the month and day from the date
    const month = new Date(date).toLocaleString('default', { month: 'long' });
    const day = new Date(date).getDate();

    // Aggregate deaths for each month and day
    if (!casesByMonthAndDate[month]) {
        casesByMonthAndDate[month] = {};
    }
    if (!casesByMonthAndDate[month][day]) {
        casesByMonthAndDate[month][day] = 0;
    }

    var x = India_Details[5][index];
    casesByMonthAndDate[month][day] += parseFloat(x); // 'deaths' data is in the third sub-array
});
console.log(casesByMonthAndDate);
const labels = [];
const parents = [];
const values = [];
for (const month in casesByMonthAndDate) {
    var sum = 0
    for (const day in casesByMonthAndDate[month]) {
        labels.push(day + month.slice(0, 3));
        parents.push(month);
        values.push(casesByMonthAndDate[month][day]);
        sum += casesByMonthAndDate[month][day]
    }
    labels.push(month);
    parents.push('India');
    values.push(sum);
}
console.log(labels)
console.log(parents)
console.log(values)

const d5 = [{
    branchvalues: 'total',
    type: 'treemap',
    labels: labels,
    textinfo: "label+value",
    parents: parents,
    values: values,
    outsidetextfont: { "size": 20, "color": "#377eb8" },
    marker: { "line": { "width": 2 } },
    pathbar: { "visible": false }
}];



var layout = {
    annotations: [{
        showarrow: false,
        text: "branchvalues: <b>remainder</b>",
        x: 0.75,
        xanchor: "center",
        y: 1.1,
        yanchor: "bottom"
    }],
    treemap: {
        branchvalues: 'total',
        // slicing: 'dice',
        // squarifyratio: 1
    },
    treemapcolorway: ['#636efa', '#ef553b', '#00cc96', '#ab63fa', '#ff7f0e', '#19d3f3', '#e763fa', '#fecb52'],
    margin: { t: 0, l: 0, r: 0, b: 0 }, // Zero margin
    height: 600, // Set the height as needed
    width: 1200, // Set the width as needed
}

Plotly.newPlot('div1', d1, layout)
Plotly.newPlot('div2', d2, layout)
Plotly.newPlot('div3', d3, layout)
Plotly.newPlot('div4', d4, layout)
Plotly.newPlot('div5', d5, layout)
Plotly.newPlot('div6', d6, layout)
