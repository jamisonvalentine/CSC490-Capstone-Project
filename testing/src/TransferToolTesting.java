
package transfertooltesting;

import com.mongodb.MongoClient;
import com.mongodb.MongoClientURI;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoCursor;
import com.mongodb.client.MongoDatabase;
import static com.mongodb.client.model.Filters.and;
import static com.mongodb.client.model.Filters.eq;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.bson.Document;
import org.openqa.selenium.By;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;
public class TransferToolTesting {

    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", ".\\driver\\chromedriver3.exe");
        WebDriver driver = new ChromeDriver();
        //Remember to change username and password
        MongoClient mongoClient = new MongoClient(new MongoClientURI("mongodb://<Username>:<password>@cluster0-shard-00-00.vppgk.mongodb.net:27017,cluster0-shard-00-01.vppgk.mongodb.net:27017,cluster0-shard-00-02.vppgk.mongodb.net:27017/ExerciseTracker?ssl=true&replicaSet=atlas-t2r24d-shard-0&authSource=admin&retryWrites=true&w=majority"));
        
        //Insert search parameters here
        Map<String, String> searchParameters = new HashMap<>();
        searchParameters.put("courseID", "MAT");
        searchParameters.put("year", "2020");
        searchParameters.put("semester", "Fall");
        searchParameters.put("type", "Online");
        
        testSearchFunction(searchParameters, driver, mongoClient);

    }
    
    /**
     * This method tests the search function of the web application by automating a search task given certain search parameters
     * and verifying the data set. 
     * The data is verified by counting the number of rows in the table, if the number of rows in the table
     * match the number of documents returned by a query to MongoDB (using the same search parameters), 
     * then the test passes. 
     * @param _searchParameters
     * @param _driver
     * @param _client
     * @return
     * @throws InterruptedException 
     */
    public static boolean testSearchFunction(Map<String, String> _searchParameters, WebDriver _driver, MongoClient _client) throws InterruptedException {
        String courseID = _searchParameters.get("courseID");
        String year = _searchParameters.get("year");
        String semester = _searchParameters.get("semester");
        String type = _searchParameters.get("type");
        
        //Web Application must be running on a local host
        _driver.navigate().to("http://localhost:3001/");
        
        
        //Set search parameters on web page.
        WebElement courseIDTextBox = _driver.findElement(By.id("courseId"));
        courseIDTextBox.sendKeys(courseID);
        
        WebElement yearDropDown = _driver.findElement(By.id("academicYear"));
        Select selectYear = new Select(yearDropDown);
        selectYear.selectByVisibleText(year);
        
        WebElement semesterDropDown = _driver.findElement(By.id("semester"));
        Select selectSemester = new Select(semesterDropDown);
        selectSemester.selectByVisibleText(semester);
        
        WebElement typeDropDown = _driver.findElement(By.id("courseType"));
        Select selectType = new Select(typeDropDown);
        selectType.selectByVisibleText(type);
        
        
        
        //Click search button 
        WebElement searchButton = _driver.findElement(By.xpath("//button[contains(.,'Search')]"));
        searchButton.click();
        
        //Wait until table is populated (at least 2 rows). If 5 seconds pass without it being populated, catch excetpion and continue.
        //If it does become populated, store number of rows in numRows variable and continue.
        List<WebElement> tableRows = new ArrayList<>();
        WebDriverWait wait = new WebDriverWait(_driver,5);
        Boolean tablePopulated = false;
        int numRows = 0;
        try {
           wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\"root\"]/div/div/div[2]/table/tbody/tr[2]"))); 
           tableRows = _driver.findElements(By.xpath("//*[@id=\"root\"]/div/div/div[2]/table/tbody/tr"));
           tablePopulated = true;
        }catch(TimeoutException e) {
            System.out.println("element not found");
            
        }
        
        if(tablePopulated) {
            numRows = tableRows.size();
        }
        
        //Perform query in MongoDB using the same search parameters
        MongoDatabase db = _client.getDatabase("ExerciseTracker");
        MongoCollection<Document> collection = db.getCollection("CCcourses");

        MongoCursor<Document> iterator = collection.find(and(eq("CourseSubject", courseID), eq( "Year", year), eq("Semester", semester), eq("Location", type))).iterator();
        int numDocuments = 0;
        while(iterator.hasNext()) {
            iterator.next();
            numDocuments++;
        }
        
        //Display test results
        System.out.println("Results:");
        System.out.println("Search parameters: " + "Course ID: " + courseID + ", Year: " + year + ", Semester: " + semester + ", Type: " + type);
        System.out.println("Number of matched documents in mongo: " + numDocuments);
        System.out.println("Number of rows in the table: " + numRows);
        if(numDocuments == numRows) {
            System.out.println("Test Pass");
            return true;
        }
        else {
            System.out.println("Test Fail");
            return false;
        }
        
    }
    
    
}
