login_input = "//*[@id='un']"
pass_input = "//*[@id='pw']"
sign_in = "//input[@type='submit']"
tasks = "//a[@href='/suite/tempo/tasks/']"
task_link = "(.//img[@alt='Unstarred'])[1]/preceding::a[2]"

rejection_reason = "(.//*[normalize-space(text()) and normalize-space(.)='Rejection reason'])[1]/following::div[3]"
rejection_Reason = "(.//*[normalize-space(text()) and normalize-space(.)='Rejection Reason'])[1]/following::div[3]"
close_reason = "(.//*[normalize-space(text()) and normalize-space(.)='Close Reason'])[1]/following::div[3]"
working = "//*[@class='appian-indicator-message']"
h1 = "//h1"