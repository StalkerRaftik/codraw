export async function GET(url = '') {
  // Default options are marked with *
  const response = await fetch(`${location.origin}/${url}`, {
    method: 'GET',
    mode: 'cors',
    cache: 'no-cache',
    credentials: 'same-origin',
    headers: {},
    referrerPolicy: 'no-referrer',
  });
  return response.json();
}

export async function POST(url = '', data = {}) {
  // Default options are marked with *
  const response = await fetch(`${location.origin}/${url}`, {
    method: 'POST',
    mode: 'cors',
    cache: 'no-cache',
    credentials: 'same-origin',
    headers: {
      'Content-Type': 'application/json'
    },
    referrerPolicy: 'no-referrer',
    body: JSON.stringify(data)
  });
  return response.json();
}