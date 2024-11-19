<header>
      <h1>Hackathon UADE - Desafíos de Python 3</h1>
      <p><strong>Desarrollado como parte de los desafíos de la Hackathon de la Universidad Argentina de la Empresa (UADE).</strong></p>
  </header>

  <section>
      <h2>Descripción del Proyecto</h2>
      <p>Este repositorio contiene una serie de ejercicios realizados durante la Hackathon organizada por la Universidad Argentina de la Empresa (UADE). Los desafíos están enfocados en resolver problemas con temáticas relacionadas a las olimpiadas, utilizando el lenguaje de programación Python 3.</p>
      <p>Los ejercicios incluyen el uso de estructuras de datos como listas, pilas y colas, y también abordan conceptos de persistencia de datos utilizando archivos de texto (.txt) para almacenar la información.</p>
  </section>

  <section>
      <h2>Ejercicios del Proyecto</h2>
      <p>El proyecto está compuesto por tres desafíos principales, cada uno enfocado en un concepto diferente:</p>
      <ul>
          <li><strong>Desafío 1: Manejo de Listas</strong> - Crear un programa que gestione una lista de atletas participantes, permitiendo agregar, eliminar y mostrar los atletas.</li>
          <li><strong>Desafío 2: Uso de Pilas</strong> - Implementar una estructura de pilas para simular las entregas de medallas en las olimpiadas, donde los atletas reciben sus medallas en un orden específico.</li>
          <li><strong>Desafío 3: Uso de Colas</strong> - Crear un sistema de colas para gestionar el registro de nuevos participantes en las olimpiadas, simulando el proceso de inscripción.</li>
      </ul>
  </section>

  <section>
      <h2>Tecnologías Utilizadas</h2>
      <ul>
          <li><strong>Python 3:</strong> El lenguaje principal utilizado para resolver los ejercicios y gestionar la lógica del programa.</li>
          <li><strong>Archivos .txt:</strong> Persistencia de datos usando archivos de texto para almacenar la información de los atletas, medallas y registros de inscripción.</li>
      </ul>
  </section>

  <section>
      <h2>Instrucciones para Ejecutar el Proyecto</h2>
      <p>Para ejecutar los ejercicios en tu máquina local, sigue los pasos a continuación:</p>
      <ol>
          <li><strong>Clona el repositorio:</strong>
              <pre>git clone https://github.com/tu_usuario/hackathon-uade-python3.git</pre>
          </li>
          <li><strong>Accede al directorio del proyecto:</strong>
              <pre>cd hackathon-uade-python3</pre>
          </li>
          <li><strong>Ejecuta el archivo Python correspondiente:</strong>
              <pre>python desafio1.py</pre>
              <pre>python desafio2.py</pre>
              <pre>python desafio3.py</pre>
          </li>
      </ol>
      <p>Cada desafío está implementado en un archivo Python separado. Puedes ejecutar cada uno individualmente desde la terminal.</p>
  </section>

  <section>
      <h2>Descripción de los Desafíos</h2>
      <h3>Desafío 1: Manejo de Listas</h3>
      <p>En este desafío, el objetivo es crear una lista de atletas y realizar las siguientes operaciones:</p>
      <ul>
          <li>Agregar nuevos atletas a la lista.</li>
          <li>Eliminar atletas que ya no participen.</li>
          <li>Mostrar todos los atletas registrados.</li>
      </ul>
      <p>La lista de atletas se guarda en un archivo de texto, para permitir su persistencia entre ejecuciones del programa.</p>

      <h3>Desafío 2: Uso de Pilas</h3>
      <p>En este ejercicio, se simula la entrega de medallas utilizando una pila (LIFO - Last In, First Out). Los atletas reciben las medallas en un orden específico, y el último atleta en recibir su medalla es el primero en ser registrado en la pila.</p>
      <p>El estado de la pila se guarda en un archivo `.txt` para que la información persista entre ejecuciones del programa.</p>

      <h3>Desafío 3: Uso de Colas</h3>
      <p>El desafío consiste en simular el registro de nuevos atletas en una cola (FIFO - First In, First Out). Los atletas se registran en orden, y el primer atleta en ingresar es el primero en ser atendido.</p>
      <p>Este sistema de cola también está implementado con persistencia, usando un archivo de texto para almacenar el estado de la cola.</p>
  </section>

  <section>
      <h2>Demostración de Funcionamiento</h2>
      <p>Cada desafío contiene ejemplos de entrada y salida para demostrar su funcionamiento:</p>
      <h3>Desafío 1: Manejo de Listas</h3>
      <p>Se puede agregar, eliminar o mostrar atletas con comandos interactivos. Ejemplo:</p>
      <pre>1. Agregar Atleta</pre>
      <pre>2. Eliminar Atleta</pre>
      <pre>3. Mostrar Atletas</pre>

      <h3>Desafío 2: Uso de Pilas</h3>
      <p>El orden de la pila se actualizará según el orden de llegada de los atletas. Ejemplo:</p>
      <pre>1. Agregar medalla a Atleta A</pre>
      <pre>2. Agregar medalla a Atleta B</pre>
      <pre>3. Mostrar medallas (último en entrar es el primero en recibirla)</pre>

      <h3>Desafío 3: Uso de Colas</h3>
      <p>Los atletas se registran en la cola y se gestionan en el orden en que se inscriben. Ejemplo:</p>
      <pre>1. Registrar Atleta C</pre>
      <pre>2. Registrar Atleta D</pre>
      <pre>3. Mostrar registro (el primero en ingresar es el primero en ser atendido)</pre>
  </section>

  <section>
      <h2>Contribuciones</h2>
      <p>Si deseas contribuir al proyecto, puedes hacer un fork del repositorio y enviar un pull request con tus cambios:</p>
      <ol>
          <li><strong>Haz un fork del repositorio:</strong> Crea una copia del proyecto en tu propio repositorio.</li>
          <li><strong>Crea una nueva rama:</strong>
              <pre>git checkout -b feature/nueva-funcionalidad</pre>
          </li>
          <li><strong>Realiza los cambios:</strong> Modifica los archivos necesarios para agregar nuevas funcionalidades o mejorar el código.</li>
          <li><strong>Haz commit de tus cambios:</strong>
              <pre>git commit -m "Descripción de los cambios realizados"</pre>
          </li>
          <li><strong>Sube tus cambios:</strong>
              <pre>git push origin feature/nueva-funcionalidad</pre>
          </li>
          <li><strong>Abre un pull request:</strong> Una vez que hayas subido tus cambios, abre un pull request para que podamos revisar y fusionar tu contribución.</li>
      </ol>
  </section>

  <section>
      <h2>Licencia</h2>
      <p>Este proyecto está bajo la licencia <strong>MIT</strong>. Puedes ver los detalles completos en el archivo <code>LICENSE</code>.</p>
  </section>

  <section>
      <h2>Agradecimientos</h2>
      <p>Agradecemos a la Universidad Argentina de la Empresa (UADE) por organizar este desafío y proporcionarnos las herramientas necesarias para completarlo. También agradecemos a los mentores y compañeros que nos ayudaron a resolver los ejercicios.</p>
  </section>

</body>
</html>
