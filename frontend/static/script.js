document.getElementById('car-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const form = e.target;
    const data = {
        brand: form.brand.value.trim(),
        model: form.model.value.trim(),
        vehicle_age: Number(form.vehicle_age.value),
        km_driven: Number(form.km_driven.value),
        seller_type: form.seller_type.value,
        fuel_type: form.fuel_type.value,
        transmission_type: form.transmission_type.value,
        mileage: Number(form.mileage.value),
        engine: Number(form.engine.value),
        max_power: Number(form.max_power.value),
        seats: Number(form.seats.value)
    };

    const resultDiv = document.getElementById('result');
    resultDiv.textContent = "Predicting...";

    fetch('/predict', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
    .then(async res => {
        let resp;
        try {
            resp = await res.json();
        } catch (err) {
            resultDiv.textContent = "Error: Invalid response from server.";
            console.error("Invalid JSON from backend:", err);
            return;
        }
        console.log("Backend response:", resp);

        if (res.ok && resp.prediction !== undefined) {
            resultDiv.textContent = `Estimated Resale Value: ₹${resp.prediction.toLocaleString()}`;
        } else if (resp.error) {
            resultDiv.textContent = "Error: " + resp.error;
        } else {
            resultDiv.textContent = "Could not predict price. Please check your input.";
        }
    })
    .catch(err => {
        resultDiv.textContent = "Error: Could not connect to server.";
        console.error("Network or server error:", err);
    });
});
