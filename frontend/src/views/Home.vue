<template>
    <div class="home">
        <h1><font-awesome-icon class="action-icon" icon="headphones" />Denon</h1>
        <div class="commands">
            <template v-for="command in commands">
                <div class="command" :key="command.code">
                    <h2>
                        <font-awesome-icon class="action-icon" :icon="command.icon" fa-spin="true" />
                        <br />
                        {{ command.name }}
                    </h2>

                    <div class="params" v-if="parametersByCommand[command.code]">
                        <template v-for="parameter in parametersByCommand[command.code]">
                            <div class="param" @click="callCommandWithParameter(parameter.url)" :key="parameter.code">
                                <font-awesome-icon class="action-icon" :icon="parameter.icon" fixed-width />
                                <br />
                                {{ parameter.name }}
                            </div>
                        </template>
                    </div>
                </div>
            </template>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import Vue from 'vue'

export default {
  name: 'Home',
  data () {
    return {
      commands: [],
      parametersByCommand: {}
    }
  },
  mounted () {
    axios.get('http://localhost:8000/api/')
      .then((response) => {
        this.commands = response.data.commands
        this.commands.forEach((command) => {
          this.fetchParameters(command.code)
        })
      })
  },
  methods: {
    fetchParameters (commandCode) {
      axios.get(`http://localhost:8000/api/command/${commandCode}/`)
        .then((response) => {
          Vue.set(this.parametersByCommand, commandCode, response.data.parameters)
        })
    },
    callCommandWithParameter (parameterUrl) {
      axios.get(`${parameterUrl}call/`)
        .then((response) => {
          console.log(response.data) // eslint-disable-line no-console
        })
    },
    queryCommandStatus (commandCode) {
      axios.get(`http://localhost:8000/api/command/${commandCode}/query/`)
        .then((response) => {
          console.log(response.data) // eslint-disable-line no-console
        })
    }
  }
}
</script>

<style lang="scss" scoped>
.commands {
  display: grid;
  grid-gap: 20px;

  @media (min-width: 500px) {
    grid-template-columns: repeat(2, 1fr);
  }

  @media (min-width: 800px) {
    grid-template-columns: repeat(4, 1fr);
  }
}

.command {
  border: 1px solid lightgray;
  border-radius: 5px;
  padding: 10px;
  text-align: center;
}

.params {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 10px;
}

.param {
  border: 1px solid lightgray;
  border-radius: 5px;
  padding: 10px;
  transition: background-color 0.3s ease;

  &:hover {
    cursor: pointer;
    background: lightgray;
    transition: background-color 0.3s ease;
  }
}

.action-icon {
  padding: 1rem;
  vertical-align: middle;
}
</style>
