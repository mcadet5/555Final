

document.addEventListener('DOMContentLoaded', function() {
    const dueDateSelect = document.querySelector('select[name="due_date"]');
    const dates = ['04-15', '06-15', '09-15', '01-15'];
    const today = new Date();
    const year = today.getFullYear() + (today.getMonth() >= 9 ? 1 : 0); // Adjust year after September

    dates.forEach(function(date) {
        const optionYear = date === '01-15' ? year + 1 : year; // Adjust for January
        const option = new Option(`${date}-${optionYear}`, `${optionYear}-${date}`);
        dueDateSelect.appendChild(option);
    });
});
