<!-- @submit.prevent="saveMovie" -->

<script setup>
    fetch("/api/v1/movies", {
    method: 'POST'
    })
    .then(function (response) {
    return response.json();
    })
    .then(function (data) {
    // display a success message
    console.log(data);
    })
    .catch(function (error) {
    console.log(error);
    });
</script>

<!-- fetch("/api/v1/movies", {
 method: 'POST'
})
 .then(function (response) {
 return response.json();
 })
 .then(function (data) {
 // display a success message
 console.log(data);
 })
 .catch(function (error) {
 console.log(error);
 }); -->