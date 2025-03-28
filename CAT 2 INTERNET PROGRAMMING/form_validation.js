document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('obituaryForm');
    
    form.addEventListener('submit', function(event) {
        let isValid = true;
        
        
        const nameInput = form.querySelector('#id_name');
        if (!nameInput.value.trim()) {
            nameInput.classList.add('is-invalid');
            isValid = false;
        } else {
            nameInput.classList.remove('is-invalid');
        }
        
        
        const dobInput = form.querySelector('#id_date_of_birth');
        const dodInput = form.querySelector('#id_date_of_death');
        
        if (!dobInput.value || !dodInput.value) {
            if (!dobInput.value) dobInput.classList.add('is-invalid');
            if (!dodInput.value) dodInput.classList.add('is-invalid');
            isValid = false;
        } else {
            dobInput.classList.remove('is-invalid');
            dodInput.classList.remove('is-invalid');
            
            
            const dob = new Date(dobInput.value);
            const dod = new Date(dodInput.value);
            
            if (dod <= dob) {
                dodInput.classList.add('is-invalid');
                dodInput.nextElementSibling.textContent = 'Date of death must be after date of birth';
                isValid = false;
            }
        }
        
        if (!isValid) {
            event.preventDefault();
            event.stopPropagation();
        }
    }, false);
});