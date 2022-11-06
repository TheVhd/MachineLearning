***Settings***
# import libraries here
Library    SeleniumLibrary
Resource    ../../RobotFramework/Resources/Elements.robot
***Variables***
${browser}    chrome
${url}    https://demo.nopcommerce.com

***Test Cases***
TestingInputBox
    open browser    ${url}    ${browser}
    Maximize Browser Window
    Title Should Be    nopCommerce demo store
    ${loginTextBox}



***Keywords***
