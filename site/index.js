// function showCategory(category) {
//     const links = {
//         it: [
//             { name: "IT Link 1", url: "http://itlink1.com" },
//             { name: "IT Link 2", url: "http://itlink2.com" },
//             // Add more IT links here
//         ],
//         food: [
//             { name: "Food Link 1", url: "http://foodlink1.com" },
//             { name: "Food Link 2", url: "http://foodlink2.com" },
//             // Add more Food links here
//         ],
//         others: [
//             { name: "Other Link 1", url: "http://otherlink1.com" },
//             { name: "Other Link 2", url: "http://otherlink2.com" },
//             // Add more Other links here
//         ]
//     };

//     const linksContainer = document.getElementById("links");
//     linksContainer.innerHTML = "";

//     links[category].forEach(link => {
//         const anchor = document.createElement("a");
//         anchor.href = link.url;
//         anchor.textContent = link.name;
//         anchor.target = "_blank";
//         linksContainer.appendChild(anchor);
//         linksContainer.appendChild(document.createElement("br"));
//     });
// }



// fetch('path_to_your_csv_file.csv')
//   .then(response => response.text())
//   .then(text => {
//     // Parse the CSV text into JSON or an array of objects
//     const products = parseCSV(text);
    
//     // Select the HTML element where you want to display the products
//     const productsContainer = document.getElementById('products-container');

//     // Clear any existing content
//     productsContainer.innerHTML = '';

//     // Iterate over the products and create HTML for each
//     products.forEach(product => {
//       const productElement = document.createElement('div');
//       productElement.className = 'product';

//       // Add the product name and price to the productElement
//       productElement.innerHTML = `<h2>${product.name}</h2><p>${product.price}</p>`;

//       // Append the productElement to the productsContainer
//       productsContainer.appendChild(productElement);
//     });
//   })
//   .catch(error => {
//     console.error('Error fetching or parsing CSV:', error);
//   });

// // A simple CSV parser function
// function parseCSV(csvText) {
//   // Split the CSV text by lines
//   const lines = csvText.split('\n');
//   // Parse each line into a product object and return an array of these objects
//   return lines.map(line => {
//     const [name, price] = line.split(',');
//     return { name, price };
//   });
// }


// Assume we have a global variable to hold all products
let allProducts = [];

fetch('C:/Users/hugod/OneDrive/Documents/Annee5_DIA/webscrapping/scrapper/scrapper/site/promotion_auchan.csv')
  .then(response => response.text())
  .then(text => {
    allProducts = parseCSV(text);
    console.log(allProducts); // This should log the parsed products
  })
  .catch(error => {
    console.error('Error fetching or parsing CSV:', error);
  });


// Show products by category
function showCategory(category) {
    // Assume categories are 'it', 'food', and 'others' in the CSV data
    const productsContainer = document.getElementById("products-container");
    productsContainer.innerHTML = "";

    // Filter products by category
    const filteredProducts = allProducts.filter(product => product.category === category);

    // Display filtered products
    filteredProducts.forEach(product => {
        const productElement = document.createElement('div');
        productElement.className = 'product';
        productElement.innerHTML = `<h2>${product.name}</h2><p>${product.price}</p>`;
        productsContainer.appendChild(productElement);
    });
}

// A simple CSV parser function
function parseCSV(csvText) {
  // Split the CSV text by lines and ignore the header
  const lines = csvText.split('\n').slice(1);
  // Parse each line into a product object and return an array of these objects
  return lines.map(line => {
    const [category, name, price] = line.split(',');
    return { category, name, price };
  });
}

// print(allProducts)