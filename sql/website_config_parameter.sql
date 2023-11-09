/**
/ HOME_PAGE_WATCH_VIDEO_EMBED_URL
**/
INSERT INTO public."Memorialmatrix_websiteconfigparameter"(
	parameter_name, parameter_value, parameter_description, is_enabled, created_date, last_updated_date)
	SELECT 'HOME_PAGE_WATCH_VIDEO_EMBED_URL', '<iframe width="600" height="400"
                      src="https://www.youtube.com/embed/YSDw3nryi2Q"
                      title="YouTube video player"
                      frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                      allowfullscreen>
              </iframe>', 'The embeddable URL of the video to used in "Watch Video" section of the home page', 't', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP
	WHERE
    NOT EXISTS (
        Select * from public."Memorialmatrix_websiteconfigparameter" where parameter_name = 'HOME_PAGE_WATCH_VIDEO_EMBED_URL'
    );

/**
/ HOME_PAGE_THEME_COLOR
**/
INSERT INTO public."Memorialmatrix_websiteconfigparameter"(
	parameter_name, parameter_value, parameter_description, is_enabled, created_date, last_updated_date)
	SELECT 'HOME_PAGE_THEME_COLOR', 'light-blue', 'The background color to be used for header and footer. The following are the allowed values.
amber, blue, grey, blue-grey, green, light-green, yellow, orange, red, pink, purple', 't', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP
	WHERE
    NOT EXISTS (
        Select * from public."Memorialmatrix_websiteconfigparameter" where parameter_name = 'HOME_PAGE_THEME_COLOR'
    );

/**
/ HOME_PAGE_PHOTO_URL
**/
INSERT INTO public."Memorialmatrix_websiteconfigparameter"(
	parameter_name, parameter_value, parameter_description, is_enabled, created_date, last_updated_date)
	SELECT 'HOME_PAGE_PHOTO_URL', 'https://images.squarespace-cdn.com/content/5f7e2983da2b802cad90ac55/6397e436-abb3-4e50-9959-10ca396de7e1/Matrix1.png?content-type=image%2Fpng', 'The URL of the photo to be  displayed in home page', 't', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP
	WHERE
    NOT EXISTS (
        Select * from public."Memorialmatrix_websiteconfigparameter" where parameter_name = 'HOME_PAGE_PHOTO_URL'
    );
	
/**
/ EMAIL_RESEARCH_INQUIRY
**/
INSERT INTO public."Memorialmatrix_websiteconfigparameter"(
	parameter_name, parameter_value, parameter_description, is_enabled, created_date, last_updated_date)
	SELECT 'EMAIL_RESEARCH_INQUIRY', 'sarah@markedbycovid.com', 'The general inquiry type email recipient.', 't', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP
	WHERE
    NOT EXISTS (
        Select * from public."Memorialmatrix_websiteconfigparameter" where parameter_name = 'EMAIL_RESEARCH_INQUIRY'
    );

/**
/ EMAIL_MESSAGE_NEW_USER
**/
INSERT INTO public."Memorialmatrix_websiteconfigparameter"(
	parameter_name, parameter_value, parameter_description, is_enabled, created_date, last_updated_date)
	SELECT 'EMAIL_MESSAGE_NEW_USER', 'Hi {{user_first_name}}, Welcome to the Marked By Covid team! Your username is {{user_email}}. 
Please contact the administrator for your credential.

Regards, Marked by Covid Admin
P.S. - This is an auto-generated email. Please do not reply to this email.', 'Email template for user registration.', 't', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP
	WHERE
    NOT EXISTS (
        Select * from public."Memorialmatrix_websiteconfigparameter" where parameter_name = 'EMAIL_MESSAGE_NEW_USER'
    );

/**
/ EMAIL_MESSAGE_MEMORIAL_APPROVED
**/
INSERT INTO public."Memorialmatrix_websiteconfigparameter"(
	parameter_name, parameter_value, parameter_description, is_enabled, created_date, last_updated_date)
	SELECT 'EMAIL_MESSAGE_MEMORIAL_APPROVED', 'Hi {{submitter_name}}, 
                  Welcome to the Marked by Covid Memorial Matrix! Your submission {{memorial_name}} is approved.
                  Please review your memorial.

Regards
 Marked by Covid Admin 

P.S. - This is an auto-generated email. Please do not reply to this email', 'Email template for what the submitter will receive when the memorial is approved.', 't', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP
	WHERE
    NOT EXISTS (
        Select * from public."Memorialmatrix_websiteconfigparameter" where parameter_name = 'EMAIL_MESSAGE_MEMORIAL_APPROVED'
    );

/**
/ EMAIL_MESSAGE_MEMORIAL_ADMIN_APPROVAL
**/
INSERT INTO public."Memorialmatrix_websiteconfigparameter"(
	parameter_name, parameter_value, parameter_description, is_enabled, created_date, last_updated_date)
	SELECT 'EMAIL_MESSAGE_MEMORIAL_ADMIN_APPROVAL', 'This memorial has been successfully submitted please review.
Memorial Name: {{mem_name}}
Memorial Description: {{mem_description}}
Memorial Founder Name: {{memfounder_name}}', 'Email template for the email that the admins get when a memorial needs to be approved.', 't', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP
	WHERE
    NOT EXISTS (
        Select * from public."Memorialmatrix_websiteconfigparameter" where parameter_name = 'EMAIL_MESSAGE_MEMORIAL_ADMIN_APPROVAL'
    );

/**
/ EMAIL_MEDIA_INQUIRY
**/
INSERT INTO public."Memorialmatrix_websiteconfigparameter"(
	parameter_name, parameter_value, parameter_description, is_enabled, created_date, last_updated_date)
	SELECT 'EMAIL_MEDIA_INQUIRY', 'christine@markedbycovid.com', 'The media inquiry type email recipient.', 't', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP
	WHERE
    NOT EXISTS (
        Select * from public."Memorialmatrix_websiteconfigparameter" where parameter_name = 'EMAIL_MEDIA_INQUIRY'
    );

/**
/ EMAIL_GENERAL_INQUIRY
**/
INSERT INTO public."Memorialmatrix_websiteconfigparameter"(
	parameter_name, parameter_value, parameter_description, is_enabled, created_date, last_updated_date)
	SELECT 'EMAIL_GENERAL_INQUIRY', 'iamanemail@markedbycovid.com', 'The general inquiry type email recipient.', 't', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP
	WHERE
    NOT EXISTS (
        Select * from public."Memorialmatrix_websiteconfigparameter" where parameter_name = 'EMAIL_GENERAL_INQUIRY'
    );

/**
/ EMAIL_ADMIN_APPROVAL
**/
INSERT INTO public."Memorialmatrix_websiteconfigparameter"(
	parameter_name, parameter_value, parameter_description, is_enabled, created_date, last_updated_date)
	SELECT 'EMAIL_ADMIN_APPROVAL', 'christine@markedbycovid.com', 'The admin approval email recipient.', 't', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP
	WHERE
    NOT EXISTS (
        Select * from public."Memorialmatrix_websiteconfigparameter" where parameter_name = 'EMAIL_ADMIN_APPROVAL'
    );

/**
/ MEMORIAL_DEFAULT_PICTURE_URL
**/
INSERT INTO public."Memorialmatrix_websiteconfigparameter"(
	parameter_name, parameter_value, parameter_description, is_enabled, created_date, last_updated_date)
	SELECT 'MEMORIAL_DEFAULT_PICTURE_URL', 'https://actionnetwork.org/user_files/user_files/000/090/886/original/MarkedByCovid_Icon.png', 'default memorial info window picture.', 't', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP
	WHERE
    NOT EXISTS (
        Select * from public."Memorialmatrix_websiteconfigparameter" where parameter_name = 'MEMORIAL_DEFAULT_PICTURE_URL'
    );

/**
/ CONTACT_US_IMAGE_URL
**/
INSERT INTO public."Memorialmatrix_websiteconfigparameter"(
	parameter_name, parameter_value, parameter_description, is_enabled, created_date, last_updated_date)
	SELECT 'CONTACT_US_IMAGE_URL', 'https://images.squarespace-cdn.com/content/v1/61ea0471aaadbc3bce33ad60/1646701015481-RCXL8FUYBHTQ9BTV95VP/Screen+Shot+1.jpeg?format=1000w', 'The default contact us image URL.', 't', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP
	WHERE
    NOT EXISTS (
        Select * from public."Memorialmatrix_websiteconfigparameter" where parameter_name = 'CONTACT_US_IMAGE_URL'
    );

/**
/ EMAIL_MESSAGE_MEMORIAL_DISAPPROVAL
**/
INSERT INTO public."Memorialmatrix_websiteconfigparameter"(
	parameter_name, parameter_value, parameter_description, is_enabled, created_date, last_updated_date)
	SELECT 'EMAIL_MESSAGE_MEMORIAL_DISAPPROVAL', 'Thank you for using the Marked by Covid Memorial Matrix! We are working to review your submission. (Reasons for delayed approval may include: duplicate entries, discrepancies in the memorial description, or insufficient information, etc.) One of our moderators will reach out to you at the email address you provided. Thank you again!', 'disapproval email template. What the submitter sees when an admin is disapproved.', 't', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP
	WHERE
    NOT EXISTS (
        Select * from public."Memorialmatrix_websiteconfigparameter" where parameter_name = 'EMAIL_MESSAGE_MEMORIAL_DISAPPROVAL'
    );