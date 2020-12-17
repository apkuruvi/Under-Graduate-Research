package instruction;
public class Instruction
{
	public static double startTime;
	public static double endTime; 
	
	public double startTimer() 
	{
        startTime = System.currentTimeMillis();
        return startTime;
    }
    public double endTimer() 
	{
        endTime = (System.currentTimeMillis() - startTime) / 1000;
        System.out.print(endTime);
        System.out.println(" seconds");
        return endTime;
    }
}
