<template>
  <div class="main">
    <header>
      <nav>
        <router-link to="/"><button class="btn">Home</button></router-link>
        <h1 class="text">Titanic Survivor Prediction App</h1>
        <router-link to="/basics"><button class="btn">Learn Basics</button></router-link>
      </nav>
    </header>

    <div class="explain">
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. Assumenda hic amet magni, sunt quae totam, dignissimos
      omnis nemo minima repudiandae voluptates neque atque in veritatis explicabo, eos culpa! Quidem autem iste
      veritatis laboriosam, dolores tempore rem quo cumque minima eaque possimus rerum aperiam error sed non eos totam
      vero quas. Corporis consequatur quas incidunt, rerum, aspernatur, eum ratione voluptatum molestias velit non
      impedit expedita quaerat illum similique laboriosam amet iste soluta? Sit ratione quos tempora eos, corrupti
      perferendis sint repudiandae delectus libero architecto odio cupiditate impedit? Aspernatur architecto sapiente
      fuga deleniti voluptatem, quasi, perspiciatis, officiis qui modi sequi iusto adipisci.
    </div>

    <main>
      <div class="history">
        <div class="header">
          <h1>History</h1>
          <p>Past 5 User search history</p>
        </div>
        <div class="display">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur
          consequuntur quisquam sequi amet veniam eius laudantium aut
          perspiciatis atque earum id quibusdam velit ad vero tenetur,
          voluptatibus debitis quo perferendis voluptates? Non aut molestiae,
          distinctio deserunt voluptatibus, omnis assumenda minima, reiciendis
          nulla minus quisquam ipsa est dolorem illum et. Ullam laudantium
          molestiae sapiente magnam tenetur eligendi ex. Ullam dicta ipsa est
          totam tenetur vero animi beatae optio molestias cum debitis, ab sint,
          deserunt, autem minima ea atque. Corrupti recusandae quia doloremque
          perspiciatis voluptatem accusamus, consectetur et excepturi provident!
          Voluptas voluptates qui deserunt, commodi doloremque ea? Officia
          cupiditate harum suscipit tempore.
        </div>
      </div>
      <div class="form">
        <form @submit.prevent="submitForm" class="form-container">
          <div class="form-group">
            <label for="dropdown1">Passenger Class</label>
            <select id="dropdown1" v-model="dropdown1" required>
              <option disabled value="">Please select one</option>
              <option value="Option 1A">First</option>
              <option value="Option 1B">Second</option>
              <option value="Option 1C">Third</option>
            </select>
          </div>

          <div class="form-group">
            <label for="dropdown2">Sex</label>
            <select id="dropdown2" v-model="dropdown2" required>
              <option disabled value="">Please select one</option>
              <option value="Option 2A">Male</option>
              <option value="Option 2B">Female</option>
              <option value="Option 2C">Other</option>
            </select>
          </div>

          <div class="form-group">
            <label for="dropdown3">Embarked</label>
            <select id="dropdown3" v-model="dropdown3" required>
              <option disabled value="">Please select one</option>
              <option value="Option 3A">Cherbourg</option>
              <option value="Option 3B">Queenstown</option>
              <option value="Option 3C">Southampton</option>
            </select>
          </div>

          <div class="form-group">
            <label for="slider1">Age (1-100):</label>
            <input type="range" id="slider1" v-model.number="slider1" min="1" max="100" required />
            <span>{{ slider1 }}</span>
          </div>

          <div class="form-group">
            <label for="slider2">Fare $ (1-1000):</label>
            <input type="range" id="slider2" v-model.number="slider2" min="1" max="1000" required />
            <span>{{ slider2 }}</span>
          </div>
          <div class="foot">
            <div class="form-group">
              <label for="dropdown4">Model Selection</label>
              <select id="dropdown4" v-model="dropdown4" required>
                <option disabled value="">Please select one</option>
                <option value="Option 4A">KNN</option>
                <option value="Option 4B">Random Forest</option>
                <option value="Option 4C">Decision Tree</option>
              </select>
            </div>


            <button type="submit" class="btn">Submit</button>

          </div>


        </form>

      </div>
    </main>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      dropdown1: "",
      dropdown2: "",
      dropdown3: "",
      dropdown4: "",
      slider1: 1,
      slider2: 1,
    };
  },
  methods: {
    async submitForm() {
      try {
        const response = await axios.post("http://127.0.0.1:8000/submit-form", {
          dropdown1: this.dropdown1,
          dropdown2: this.dropdown2,
          dropdown3: this.dropdown3,
          dropdown4: this.dropdown4,
          slider1: this.slider1,
          slider2: this.slider2,
        });
        console.log(response.data);
      } catch (error) {
        console.error("Error submitting form:", error);
      }
    },
  },
};
</script>

<style scoped>
* {
  padding: 0;
  margin: 0;
  outline: none;
  border: none;
  box-sizing: border-box;
  color: #fff;
}

.main {
  font-family: "Poppins", sans-serif;
  background-color: #18181b;
  padding-top: 2vh;
  color: #fff;
}

header {
  background-color: #1f2937;
  padding: 2rem;
}

nav {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

h1 .text {
  align-items: center;
  margin-bottom: 1.5rem;
}

.btn {
  width: 15rem;
  padding: 1rem 2rem;
  font-size: 1rem;
  color: #fff;
  background-color: #1d4ed8;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn:hover {
  background-color: #1e40af;
}

.explain{
  padding: 2rem;
}


main {
  display: flex;
  flex-direction: row;
}

.history {
  display: flex;
  flex-direction: column;
  width: 40%;
  border: 2px solid white;
  border-radius: 50px;
  margin: 2rem;
}

.history .header {
  padding: 1rem;
  margin: 1rem;
  border-radius: 50px;
  background-color: rgba(0, 0, 255, 0.128);
  font-size: 1.1rem;
}

.history .display {
  padding: 1rem;
  margin: 1rem;
  border: 2px solid white;
  border-radius: 40px;
  min-height: 300px;
}

.form {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 60%;
  margin: 2rem 1.5rem 1.5rem 0.5rem;
}

.form-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  padding: 2rem;
  background-color: #1f2937;
  border: 2px solid white;
  border-radius: 50px;
}

.form-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 1.7rem;
}

label {
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
  font-weight: 600;
}

select,
input[type="range"] {
  padding: 1rem;
  border-radius: 25px;
  border: 1px solid #ffffff;
  background-color: #111827;
  color: #fff;
  font-size: 1rem;
  outline: none;
  transition: all 0.3s ease;
}

select:focus,
input[type="range"]:focus {
  border-color: #1b6ad3;
}

input[type="range"] {
  /* -webkit-appearance: none; */
  appearance: none;
  width: 100%;
  background: transparent;
}

input[type="range"]::-webkit-slider-runnable-track {
  width: 100%;
  height: 3px;
  background: #0ccd12;
  border-radius: 5px;
}

input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 10px;
  height: 20px;
  background: #1d4ed8;
  border-radius: 100% 100% 0% 0%;
  cursor:grab;
}

/* input[type="range"]::-moz-range-track {
  width: 100%;
  height: 10px;
  background: #1d4ed8;
  border-radius: 5px;
}

input[type="range"]::-moz-range-thumb {
  width: 20px;
  height: 20px;
  background: #1d4ed8;
  border-radius: 50%;
  cursor: pointer;
} */

input[type="range"]::-ms-track {
  width: 100%;
  height: 5px;
  background: transparent;
  border-color: transparent;
  border-width: 5px 0;
  color: transparent;
}

/* input[type="range"]::-ms-fill-lower,
input[type="range"]::-ms-fill-upper {
  background: #1d4ed8;
} */

/* input[type="range"]::-ms-thumb {
  width: 20px;
  height: 20px;
  background: #1d4ed8;
  border-radius: 50%;
  cursor: pointer;
} */

.foot {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
}
</style>
