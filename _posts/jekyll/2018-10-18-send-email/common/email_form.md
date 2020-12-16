```html
<form name="sentMessage" id="contactForm" novalidate action="https://formspree.io/{{ site.email }}" method="post">
    <input type="hidden" name="_subject" value="블로그에서 새로운 연락이 왔습니다." />
    <input type="text" name="_gotcha" style="display:none" />
    <div class="control-group">
        <div class="form-group floating-label-form-group controls">
        <label>{{ page.input_name }}</label>
        <input type="text" class="form-control" placeholder="{{ page.input_name }}" id="name" name="name" required data-validation-required-message="{{ page.input_name_error }}">
        <div class="help-block text-danger"></div>
        </div>
        <div class="form-group floating-label-form-group controls">
        <label>{{ page.input_email }}</label>
        <input type="email" class="form-control" placeholder="{{ page.input_email }}" id="email" name="email" required data-validation-validemail-message="{{ page.input_email_validation_meesage }}" data-validation-required-message="{{ page.input_email_error }}">
        <div class="help-block text-danger"></div>
        </div>
        <div class="form-group floating-label-form-group controls">
        <label>{{ page.input_message }}</label>
        <textarea rows="5" class="form-control" placeholder="{{ page.input_message }}" id="message" name="message" required data-validation-required-message="{{ page.input_message_error }}"></textarea>
        <div class="help-block text-danger"></div>
        </div>
    </div>
    <br>
    <div id="success"></div>
    <div class="form-group">
        <button type="submit" class="btn btn-primary" id="sendMessageButton">Send</button>
    </div>
</form>
```