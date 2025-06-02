<h1>Monster Battle Game - Part 1</h1>

<p>This is a simple battle game between two monsters developed in Python. The entire game runs in the console, where the player enters commands to attack the enemy.</p>

<hr />

<h2>Description</h2>
<p>The player and an enemy monster both start with 500 health points. On each turn, the player chooses an ability to attack (Claw, Tail, or Special Attack), and the enemy monster responds with a random attack. Each move has a success probability and a specific damage value. The battle continues until one of the monsters loses all its health.</p>

<hr />

<h2>How it works</h2>
<ul>
  <li>The player's name is requested.</li>
  <li>The current health points of both monsters are displayed.</li>
  <li>The player chooses an attack by typing:
    <ul>
      <li><code>1</code> for Claw (90% success, 10 damage)</li>
      <li><code>2</code> for Tail (70% success, 50 damage)</li>
      <li><code>3</code> for Special Attack (15% success, 100 damage)</li>
    </ul>
  </li>
  <li>It is randomly determined whether the attack hits based on its probability.</li>
  <li>If the attack hits, the enemy monster’s health is reduced accordingly.</li>
  <li>The enemy then makes a random attack with similar probabilities and damage values.</li>
  <li>This cycle repeats until one of the monsters reaches 0 or less health points.</li>
  <li>At the end, a graphical window is shown with the result (victory or defeat).</li>
</ul>

<hr />

<h2>Requirements</h2>
<ul>
  <li>Python 3.10+ (due to use of <code>match</code> / <code>case</code>)</li>
  <li><code>tkinter</code> module to display the result windows</li>
</ul>

<hr />

<h2>How to run</h2>
<ol>
  <li>Run the script.</li>
  <li>Enter your name when prompted.</li>
  <li>Choose an attack by typing <code>1</code>, <code>2</code>, or <code>3</code> on each turn.</li>
  <li>Read the console messages to see the results of the attacks.</li>
  <li>At the end, a window will appear showing whether you won or lost.</li>
</ol>

<hr />

<h1>Monster Battle Game - Part 2</h1>

<p>This is the second part of the monster battle game. Unlike the first version, this one is controlled directly through the keyboard, making the gameplay smoother and faster.</p>

<hr />

<h2>What's new compared to Part 1</h2>
<ul>
  <li>No more console menus to choose attacks.</li>
  <li>The player can now press <strong>1</strong>, <strong>2</strong>, or <strong>3</strong> to attack using:
    <ul>
      <li><strong>1</strong>: Claw (90% success, 10 damage)</li>
      <li><strong>2</strong>: Tail (70% success, 50 damage)</li>
      <li><strong>3</strong>: Special (15% success, 100 damage)</li>
    </ul>
  </li>
  <li>The <code>keyboard</code> module is used to detect key events.</li>
  <li>The battle continues until one of the monsters loses all its health, and the result is displayed in a graphical window.</li>
</ul>

<hr />

<h2>Requirements</h2>
<ul>
  <li>Python 3.10+</li>
  <li><code>tkinter</code> module (usually included with Python)</li>
  <li>External <code>keyboard</code> module (install with <code>pip install keyboard</code>)</li>
  <li>Must be run as administrator or with elevated privileges on Windows (required by <code>keyboard</code> module)</li>
</ul>

<hr />

<h2>How to play</h2>
<ol>
  <li>Run the script in a terminal or console.</li>
  <li>Enter your name when prompted.</li>
  <li>During your turn, press:
    <ul>
      <li><kbd>1</kbd>: Claw</li>
      <li><kbd>2</kbd>: Tail</li>
      <li><kbd>3</kbd>: Special</li>
    </ul>
  </li>
  <li>Observe the results of your attack in the console.</li>
  <li>Then, the enemy monster will perform a random attack.</li>
  <li>This cycle repeats until one of the monsters reaches 0 or less HP.</li>
  <li>A graphical window will show a victory or defeat message.</li>
</ol>

<hr />




