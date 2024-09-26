document.addEventListener("DOMContentLoaded", function() {
    // Access the data from the 'chartData' div
    const chartDataDiv = document.getElementById('yearly-revenue');
    const months = JSON.parse(chartDataDiv.getAttribute('data-months'));  // Parse JSON string into array
    const totalRevenue = JSON.parse(chartDataDiv.getAttribute('data-total-revenue')); // Parse JSON

    // Create the line chart using the Chart.js library
    const ctx = document.getElementById('revenueChart').getContext('2d');
    const revenueChart = new Chart(ctx, {
        type: 'line', // Chart type
        data: {
            labels: months, // X-axis labels (months)
            datasets: [{
                label: 'Total Revenue per Month', // Label for the dataset
                data: totalRevenue, // Y-axis data (revenue)
                borderColor: 'rgba(75, 192, 192, 1)', // Line color
                backgroundColor: 'rgba(75, 192, 192, 0.2)', // Fill under the line
                borderWidth: 2, // Line thickness
                tension: 0.2, // Line smoothness
                pointRadius: 4, // Point size
                pointBackgroundColor: 'rgba(75, 192, 192, 1)', // Point color
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Month' // X-axis title
                    }
                },
                y: {
                    beginAtZero: false,
                    min: 1000,
                    title: {
                        display: true,
                        text: 'Revenue (in $)' // Y-axis title
                    }
                }
            },
            plugins: {
                legend: {
                    labels: {
                        font: {
                            size: 18, // Increase the font size of the label
                        }
                    }
                }
            }
        }
    });
});


document.addEventListener("DOMContentLoaded", function() {
    // Access the data from the 'chartData' div
    const chartDataDiv = document.getElementById('quarterly-revenue');
    const pieChartValues = JSON.parse(chartDataDiv.getAttribute('data-pie-chart')); // Parse JSON

    // Create the pie chart using the Chart.js library
    const ctx = document.getElementById('quarterlySalesChart').getContext('2d');
    const quarterlySalesChart = new Chart(ctx, {
        type: 'pie', // Chart type
        data: {
            labels: ['First Quarter', 'Second Quarter', 'Third Quarter', 'Fourth Quarter'],
            datasets: [{
                label: 'Quarterly Sales',
                data: pieChartValues,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.5)',
                    'rgba(54, 162, 235, 0.5)',
                    'rgba(255, 206, 86, 0.5)',
                    'rgba(75, 192, 192, 0.5)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false, // Ensure the chart can adjust to container size
            plugins: {
                legend: {
                    display: true,
                    position: 'top',
                    labels: {
                        font: {
                            size: 16
                        }
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                        const dataset = context.dataset;
                        const total = dataset.data.reduce((a, b) => a + b, 0);
                        const value = dataset.data[context.dataIndex];
                        const percentage = ((value / total) * 100).toFixed(2) + '%';
                        return context.label + ': ' + value + ' (' + percentage + ')';
                        }
                    }
                }
            }
        }
    });
});


document.addEventListener("DOMContentLoaded", function() {
    // Access the data from the 'chartData' div
    const chartDataDiv = document.getElementById('items-sold');
    const months = JSON.parse(chartDataDiv.getAttribute('items-months'));  // Parse JSON string into array
    const itemsSoldValues = JSON.parse(chartDataDiv.getAttribute('data-items-sold')); // Parse JSON

    // Create the line chart using the Chart.js library
    const ctx = document.getElementById('itemsSoldChart').getContext('2d');
    const itemsSoldChart = new Chart(ctx, {
        type: 'line', // Chart type
        data: {
            labels: months, // X-axis labels (months)
            datasets: [{
                label: 'Items Sold Per Month', // Label for the dataset
                data: itemsSoldValues, // Y-axis data (revenue)
                borderColor: 'rgba(75, 192, 192, 1)', // Line color
                backgroundColor: 'rgba(75, 192, 192, 0.2)', // Fill under the line
                borderWidth: 2, // Line thickness
                tension: 0.2, // Line smoothness
                pointRadius: 4, // Point size
                pointBackgroundColor: 'rgba(75, 192, 192, 1)', // Point color
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Month' // X-axis title
                    }
                },
                y: {
                    beginAtZero: false,
                    min:100,
                    max:285,
                    title: {
                        display: true,
                        text: 'Number of Items (Quatity)' // Y-axis title
                    }
                }
            },
            plugins: {
                legend: {
                    labels: {
                        font: {
                            size: 18, // Increase the font size of the label
                        }
                    }
                }
            }
        }
    });
});


document.addEventListener("DOMContentLoaded", function() {
    // Access the data from the 'chart-data' div
    const chartDataDiv = document.getElementById('revenue-per-item');
    const monthlyData = JSON.parse(chartDataDiv.getAttribute('items-revenue-per-month')); // Parse JSON

    // Extract the data from the JSON object
    const months = monthlyData.Month;
    const notebook = monthlyData.Notebook;
    const pen = monthlyData.Pen;
    const coffeeMug = monthlyData["Coffee Mug"];
    const deskLamp = monthlyData["Desk Lamp"];
    const calendar = monthlyData.Calendar;

    // Create the bar chart using Chart.js
    const ctx = document.getElementById('revenuePerItem').getContext('2d');
    const barChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: months, // X-axis labels
            datasets: [
                {
                    label: 'Notebook',
                    data: notebook,
                    backgroundColor: 'rgba(255, 99, 132, 0.5)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                },
                {
                    label: 'Pen',
                    data: pen,
                    backgroundColor: 'rgba(54, 162, 235, 0.5)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                },
                {
                    label: 'Coffee Mug',
                    data: coffeeMug,
                    backgroundColor: 'rgba(255, 206, 86, 0.5)',
                    borderColor: 'rgba(255, 206, 86, 1)',
                    borderWidth: 1
                },
                {
                    label: 'Desk Lamp',
                    data: deskLamp,
                    backgroundColor: 'rgba(75, 192, 192, 0.5)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                },
                {
                    label: 'Calendar',
                    data: calendar,
                    backgroundColor: 'rgba(153, 102, 255, 0.5)',
                    borderColor: 'rgba(153, 102, 255, 1)',
                    borderWidth: 1
                }
            ]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Months' // X-axis label
                    }
                },
                y: {
                    beginAtZero: true, // Ensures Y-axis starts from 0
                    title: {
                        display: true,
                        text: 'Profit Made (in US Dollars)' // Y-axis label
                    }
                }
            }
        }
    });
});

document.addEventListener("DOMContentLoaded", function() {
    // Access the data from the 'items-sold-bar' div
    const chartDataDiv = document.getElementById('items-sold-bar');
    const monthlyData = JSON.parse(chartDataDiv.getAttribute('items-sold-per-month')); // Parse JSON

    // Extract the data from the JSON object
    const months = monthlyData.Month;
    const notebook = monthlyData.Notebook;
    const pen = monthlyData.Pen;
    const coffeeMug = monthlyData["Coffee Mug"];
    const deskLamp = monthlyData["Desk Lamp"];
    const calendar = monthlyData.Calendar;

    // Create the bar chart using Chart.js
    const ctx = document.getElementById('itemsSoldBarChart').getContext('2d');
    const barChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: months, // X-axis labels
            datasets: [
                {
                    label: 'Notebook',
                    data: notebook,
                    backgroundColor: 'rgba(255, 99, 132, 0.5)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                },
                {
                    label: 'Pen',
                    data: pen,
                    backgroundColor: 'rgba(54, 162, 235, 0.5)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                },
                {
                    label: 'Coffee Mug',
                    data: coffeeMug,
                    backgroundColor: 'rgba(255, 206, 86, 0.5)',
                    borderColor: 'rgba(255, 206, 86, 1)',
                    borderWidth: 1
                },
                {
                    label: 'Desk Lamp',
                    data: deskLamp,
                    backgroundColor: 'rgba(75, 192, 192, 0.5)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                },
                {
                    label: 'Calendar',
                    data: calendar,
                    backgroundColor: 'rgba(153, 102, 255, 0.5)',
                    borderColor: 'rgba(153, 102, 255, 1)',
                    borderWidth: 1
                }
            ]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Months' // X-axis label
                    }
                },
                y: {
                    beginAtZero: true, // Ensures Y-axis starts from 0
                    title: {
                        display: true,
                        text: 'Number of Items Sold' // Y-axis label
                    }
                }
            }
        }
    });
});