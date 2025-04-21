

wall_l = Sprite(5,200,10,400,"s")
wall_r = Sprite(495,200,10,400,"s")
floor = Sprite(250,0,500,20,"s")

wall_l.color = "cornflowerblue"
wall_r.color = "yellow"
floor.color = "navy"

#lists for colours and sizes
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
sizes = [12, 24, 36, 48, 60, 72]


def setup():
  createCanvas(500,400)
  textAlign(CENTER, CENTER)
def draw():
  background("white")
  drawTickAxes(1, 50, "black", "black", "black")
  
  # Define x positions for 6 circles (equidistant across the canvas)
  positions = [75, 150, 225, 300, 375, 450]
  
  # Dictionary mapping color names to emoji representations
  color_emojis = {
      "red": "🔴",
      "orange": "🟠",
      "yellow": "🟡",
      "green": "🟢",
      "blue": "🔵",
      "purple": "🟣"
  }

  # Draw circles based on the colours list and apply corresponding sizes
  for i, colour in enumerate(colours):
    if colour in color_emojis:
      textSize(sizes[i])  # Set text size based on the sizes list
      text(color_emojis[colour], positions[i], 200)  # Display the corresponding em