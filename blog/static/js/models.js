/*
 * Data Models
 */

function PostImage(data) {
    var self = this;

    self.image = ko.observable(data.image);
}

function Post(data) {
    var self = this;

    self.id = data.id;
    self.title = ko.observable(data.title);
    self.content = ko.observable(data.content);
    self.slug = ko.observable(models.slug);
    self.date = ko.observable(models.date);
    self.published = ko.observable(models.published);
    self.images = ko.observableArray();
}
