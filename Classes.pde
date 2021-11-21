public class Point
{
  public float X;
  public float Y;
  
  public Point(float x, float y)
  {
    this.X = x;
    this.Y = y;
  }
}

public class Angle
{
  public Point Left;
  public Point Center;
  public Point Right;
  
  public Angle(Point left, Point center, Point right)
  {
    this.Left = left;
    this.Center = center;
    this.Right = right;
  }
  
  public void DrawAngle()
  {
    line(this.Left.X, this.Left.Y, this.Center.X, this.Center.Y);
    line(this.Center.X, this.Center.Y, this.Right.X, this.Right.Y);
  }
  
  public void DrawLines(int n)
  {
    for (int i = 1; i < n; i++)
    {
      float x1 = this.Left.X + ((this.Center.X - this.Left.X) / n) * i;
      float y1 = this.Left.Y + ((this.Center.Y - this.Left.Y) / n) * i;
      float x2 = this.Right.X + ((this.Center.X - this.Right.X) / n) * i;
      float y2 = this.Right.Y + ((this.Center.Y - this.Right.Y) / n) * i;
      line(x1, y1, x2, y2);
    }
  }
}

public class Star
{
  public Angle Top;
  public Angle Right;
  public Angle BottomRight;
  public Angle BottomLeft;
  public Angle Left;
  
  public Star(Angle top, Angle right, Angle bottomRight, Angle bottomLeft, Angle left)
  {
    this.Top = top;
    this.Right = right;
    this.BottomRight = bottomRight;
    this.BottomLeft = bottomLeft;
    this.Left = left;
  }
  
  public void DrawStar()
  {
    this.Top.DrawAngle();
    this.Right.DrawAngle();
    this.BottomRight.DrawAngle();
    this.BottomLeft.DrawAngle();
    this.Left.DrawAngle();
  }
  
  public void DrawLines(int n)
  {
    this.Top.DrawLines(n);
    this.Right.DrawLines(n);
    this.BottomRight.DrawLines(n);
    this.BottomLeft.DrawLines(n);
    this.Left.DrawLines(n);
  }
}
