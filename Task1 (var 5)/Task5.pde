 void setup() {
  size(900, 900);
  background(255);
  surface.setTitle("Patrick Star");
  
  Point topP = new Point(width/2, 0);
  Point topRightP = new Point(0.65 * width, height/3);
  Point rightP = new Point(width, height/3);
  Point rightCloseP = new Point(0.7 * width, 0.55 * height);
  Point bottomRightP = new Point(0.8 * width, 0.9 * height);
  Point bottomP = new Point(width / 2, (2 * height) / 3);
  Point bottomLeftP = new Point(0.2 * width, 0.9 * height);
  Point leftCloseP = new Point(0.3 * width, 0.55 * height);
  Point leftP = new Point(0, height/3);
  Point topLeftP = new Point(0.35 * width, height/3);
  
  Angle top = new Angle(topLeftP, topP, topRightP);
  Angle right = new Angle(topRightP, rightP, rightCloseP);
  Angle bottomRight = new Angle(rightCloseP, bottomRightP, bottomP);
  Angle bottomLeft = new Angle(bottomP, bottomLeftP, leftCloseP);
  Angle left = new Angle(leftCloseP, leftP, topLeftP);
  
  star = new Star(top, right, bottomRight, bottomLeft, left);
  
  star.DrawStar();
  frameRate(10);
  textSize(height/20);
}
  Star star;
  int N = 1;
  
void draw() {
  if (mousePressed && mouseButton == LEFT) {
    N++;
  }
  else if (mousePressed && mouseButton == RIGHT && N > 1) {
    N--;
  }
  background(255);
  text("N = " + N, width * 0.45, height * 0.95);
  fill(0);
  star.DrawStar();
  star.DrawLines(N);
}
