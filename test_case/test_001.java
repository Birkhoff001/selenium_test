<pre name="code" class="java">package com.beyondtest;

import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

public class TestOrder{
	WebDriver wd;
	@Test
	pubilc void test() throws InterruptedException{
	wd = new FirefoxDriver();
	wd.get("http://www.12306.cn/mormhweb/");
	Thread.sleep(100);
	wd.findElement(By.cssSelecor("k2")).click();
	Thread.sleep(100);
	wd.switchTo().frame("iframepage");
}
}
