import $t from "@/i18n";

function isIterableObject(value) {
  return typeof value !== 'string' && Symbol.iterator in Object(value);
}

export function parseResponseException(e) {
  let respContent = "";
  if (!e.response) {
    return 'Соединение с сервером потеряно, попробуйте еще раз.';
  }
  if (e.response.status >= 500) {
    return `Случилась ошибка на сервере. Сообщите об этой проблеме администратору.\nСтатус ошибки: ${e.response.status}`;
  }
  console.log(e.response.status);
  for (const errors of Object.values(e.response.data)) {
    if (!isIterableObject(errors)) {
      respContent += `- ${$t(errors)}\n`;
      continue;
    }
    errors.forEach((error) => (respContent += `- ${$t(error)}\n`));
  }
  return respContent || JSON.stringify(e.response);
}
