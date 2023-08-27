I have this Django template that display the "data" in a table.

<h1>Table of {{ table_title }}</h1>
<table class="table table-hover">
    <thead>
        <tr>
            {% for field in data.0 %}
            <th>{{ field }}</th>
            {% endfor %}
        </tr>
    </thead>
    <tbody>
        {% for row in data %}
        <tr>
            {% for value in row.values %}
            <td>{{ value }}</td>
            {% endfor %}
        </tr>
        {% endfor %}
    </tbody>
</table>

I want to pass in multiple tables as a dictionary and display them.

