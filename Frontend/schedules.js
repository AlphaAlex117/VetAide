const form = document.querySelector('form');
function post(url, jsonData) {
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(jsonData),
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response data here
        console.log(data);
    })
    .catch(error => {
        // Handle any errors here
        console.error(error);
    });
}

form.addEventListener('submit', (event) => {
    event.preventDefault();
    
    const operationCategory = document.getElementById('operation-category').value;
    const veterinarian = document.getElementById('veterinarian').value;
    const owner = document.getElementById('owner').value;
    const appointmentDate = document.getElementById('appointment-date').value;
    const patientName = document.getElementById('patient-name').value;
    
    const formData = {
        operationCategory,
        veterinarian,
        owner,
        appointmentDate,
        patientName
    };
    
    
    document.getElementById('schedules').innerHTML = JSON.stringify(formData);

    const url = 'http:///127.0.0.1:3000/';
    // Call the post function with the desired URL and JSON data
    post(url+"make_appointment", formData);
});




  
