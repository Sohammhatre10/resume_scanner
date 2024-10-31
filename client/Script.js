function uploadResume() {
  const fileInput = document.getElementById('resume-upload');
  const file = fileInput.files[0];
  const selectedModel = document.getElementById('model-select').value;
  const selectedAction = document.getElementById('action-select').value;

  if (!file && selectedAction === 'check') {
  
  if (!file) {
    alert('Please select a file to upload.');
    return;
  }


  alert(`You selected to ${selectedAction} a resume using ${selectedModel}.`);
  // Add further logic based on selected action and model
  alert(`Your resume is being scanned using ${selectedModel}! Results will be available shortly.`);
  // Add file upload and processing logic here, including selected model
}
