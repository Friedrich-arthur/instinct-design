document.querySelectorAll('[data-copy]').forEach((button) => {
  if (!navigator.clipboard?.writeText) return;
  const command = document.getElementById(button.dataset.copy);
  const status = button.closest('.install-panel').querySelector('[data-copy-status]');
  const label = button.textContent;
  button.hidden = false;
  button.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(command.textContent);
      button.textContent = button.dataset.copied;
      status.textContent = button.dataset.success;
      setTimeout(() => { button.textContent = label; }, 2000);
    } catch {
      status.textContent = button.dataset.failed;
    }
  });
});

document.querySelectorAll('[data-exercise]').forEach((exercise) => {
  const fieldset = exercise.querySelector('fieldset');
  const conditions = Array.from(fieldset.querySelectorAll('input[type="checkbox"]'));
  const result = exercise.querySelector('[data-result]');
  const detail = exercise.querySelector('[data-result-detail]');
  const update = () => {
    const interrupt = conditions.every((condition) => condition.checked);
    exercise.dataset.interrupt = String(interrupt);
    result.textContent = interrupt ? exercise.dataset.yes : exercise.dataset.no;
    detail.textContent = interrupt ? exercise.dataset.yesDetail : exercise.dataset.noDetail;
  };
  conditions.forEach((condition) => {
    condition.checked = false;
    condition.addEventListener('change', update);
  });
  fieldset.hidden = false;
  update();
});
