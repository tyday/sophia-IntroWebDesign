fetch('products.json')
  .then(response => response.json())
  .then(data => {
    const productList = document.getElementById('product-list');
    const template = Handlebars.compile(document.getElementById('product-template').innerHTML);
    const html = template({products: data});
    productList.innerHTML = html;
  });